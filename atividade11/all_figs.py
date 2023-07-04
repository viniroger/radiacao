# Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pvlib
import unidecode

def make_sunpath(loc):
  '''
  Calculate sun path
  for a location (latitude, longitude, altitude, time zone)
  '''
  times = pd.date_range('2015-01-01 00:00:00', '2016-01-01', freq='H', tz=loc.tz)
  solpos = pvlib.solarposition.get_solarposition(times, loc.latitude, loc.longitude)
  # Remover horários noturnos
  solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]

  ax = plt.subplot(1, 1, 1, projection='polar')
  # Desenhar os loops do analema
  points = ax.scatter(np.radians(solpos.azimuth),
                      solpos.apparent_zenith,
                      s=2,
                      label=None,
                      c=solpos.index.dayofyear)
  ax.figure.colorbar(points)

  # Imprimir rótulos de horas
  for hour in np.unique(solpos.index.hour):
    # Escolher a posição do rótulo pelo menor raio para cada hora
    subset = solpos.loc[solpos.index.hour == hour, :]
    r = subset.apparent_zenith
    pos = solpos.loc[r.idxmin(), :]
    ax.text(np.radians(pos['azimuth']), pos['apparent_zenith'], str(hour))

  # Imprimir dias individuais
  for date in pd.to_datetime(['2015-03-20', '2015-06-21', '2015-12-22']):
    times = pd.date_range(date, date + pd.Timedelta('24h'), freq='5min', tz=loc.tz)
    solpos = pvlib.solarposition.get_solarposition(times, loc.latitude, loc.longitude)
    solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]
    label = date.strftime('%Y-%m-%d')
    ax.plot(np.radians(solpos.azimuth), solpos.apparent_zenith, label=label)

  ax.figure.legend(loc='upper left')
  ax.title.set_text(loc.name)

  # Alterar as coordenadas para ser como uma bússola
  ax.set_theta_zero_location('N')
  ax.set_theta_direction(-1)
  ax.set_rmax(90)

  # Exibir a imagem (janela/output/corpo)
  #plt.show()
  # Salvar imagem em arquivo - tirar espaços e sinais gráficos
  loc_name = loc.name.replace(' ', '')
  loc_name = unidecode.unidecode(loc_name)
  plt.savefig(f'figs/sunpath_{loc_name}.png', bbox_inches='tight')
  plt.close()

def csi_Ineichen(loc, times):
  '''
  Calculate clear sky irradiance using Ineichen model
  for a location (latitude, longitude, altitude, time zone)
  '''
  day_str = times[0].strftime('%Y-%m-%d')
  cs = loc.get_clearsky(times)
  ax = cs.plot(linestyle=':', marker='o')
  ax.grid()
  plt.ylabel('Irradiancia $W/m^2$')
  plt.title(f'Ineichen climatological turbidity - {loc.name} - {day_str}')
  #plt.show()
  # Salvar imagem em arquivo - tirar espaços e sinais gráficos
  loc_name = loc.name.replace(' ', '')
  loc_name = unidecode.unidecode(loc_name)
  plt.savefig(f'figs/Ineichen_{loc_name}.png', bbox_inches='tight')
  plt.close()

def csi_Solis(loc, times):
  '''
  Calculate clear sky irradiance using simplified Solis model
  for a location (latitude, longitude, altitude, time zone)
  Consider: AOD 700 nm; precipitable water; pressure (altitude)
  '''
  day_str = times[0].strftime('%Y-%m-%d')
  solpos = pvlib.solarposition.get_solarposition(times, loc.latitude, loc.longitude)
  apparent_elevation = solpos['apparent_elevation']
  aod700 = 0.1
  precipitable_water = 1
  pressure = pvlib.atmosphere.alt2pres(loc.altitude)
  dni_extra = pvlib.irradiance.get_extra_radiation(times)
  # an input is a Series, so solis is a DataFrame
  solis = pvlib.clearsky.simplified_solis(apparent_elevation, aod700, precipitable_water, pressure, dni_extra)
  ax = solis.plot(linestyle=':', marker='o')
  ax.grid()
  ax.set_ylabel('Irradiance $W/m^2$')
  ax.set_title(f'Simplified Solis Clear Sky Model - {loc.name} - {day_str}')
  ax.legend(loc=2)
  # Salvar imagem em arquivo - tirar espaços e sinais gráficos
  loc_name = loc.name.replace(' ', '')
  loc_name = unidecode.unidecode(loc_name)
  plt.savefig(f'figs/Solis_{loc_name}.png', bbox_inches='tight')
  plt.close()

# Loop para todos os locais
df = pd.read_csv('locais_estudo.csv')
for index, row in df.iterrows():
  # Definir espaço e tempo
  loc = pvlib.location.Location(row['Latitude'], row['Longitude'], tz=row['Fuso horário'], altitude=row['Altitude'], name=row['Nome do local'])
  print(loc.name)
  #tz = 'UTC'
  times = pd.date_range(start='2015-02-08 01:00:00', end='2015-02-08 23:00:00', freq='5min', tz=loc.tz)
  # Aplicar métodos
  make_sunpath(loc)
  csi_Ineichen(loc, times)
  csi_Solis(loc, times)
  #exit()