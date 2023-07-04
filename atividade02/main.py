# Importar bibliotecas
from pvlib import solarposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tz = 'UTC'
lat, lon = -3.21, -53.823

times = pd.date_range('2015-01-01 00:00:00', '2016-01-01', freq='H', tz=tz)
solpos = solarposition.get_solarposition(times, lat, lon)
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
  times = pd.date_range(date, date + pd.Timedelta('24h'), freq='5min', tz=tz)
  solpos = solarposition.get_solarposition(times, lat, lon)
  solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]
  label = date.strftime('%Y-%m-%d')
  ax.plot(np.radians(solpos.azimuth), solpos.apparent_zenith, label=label)

ax.figure.legend(loc='upper left')

# Alterar as coordenadas para ser como uma bússola
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rmax(90)

# Exibir a imagem (janela/output/corpo)
#plt.show()
# Salvar imagem em arquivo
plt.savefig('sunpath.png', bbox_inches='tight')