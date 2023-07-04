import itertools
import numpy as np
import pvlib
from pvlib.location import Location
import pandas as pd
import matplotlib.pyplot as plt

# Methods

def convert_aod(info1, info2):
  '''
  Calculates Angstrom exponent and AOD from two wavelengths
  info = (wavelength, AOD at this wavelength)
  '''
  alpha_exponent = pvlib.atmosphere.angstrom_alpha(info1[1], info1[0], info2[1], info2[0])
  aod700nm = pvlib.atmosphere.angstrom_aod_at_lambda(info1[1], info1[0], alpha_exponent, 700)
  print(f'Angstrom exponent = {alpha_exponent:.2f}')
  print(f'AOD at 700-nm = {aod700nm:.2f}')

def clear_sky(loc, times):
  '''
  Calculate clear sky irradiance using simplified Solis model
  for a location (latitude, longitude, altitude, time zone)
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
  ax.set_ylabel('Irradiance $W/m^2$')
  ax.set_title(f'Simplified Solis Clear Sky Model - {day_str}')
  ax.legend(loc=2);
  plt.savefig('cs.png', bbox_inches='tight')

def compare(loc, times, aod700, precipitable_water):
  '''
  Compare clear sky model using AOD and PW given values
  for a location (latitude, longitude, altitude, time zone)
  '''
  solpos = pvlib.solarposition.get_solarposition(times, loc.latitude, loc.longitude)
  apparent_elevation = solpos['apparent_elevation']
  pressure = pvlib.atmosphere.alt2pres(loc.altitude)
  dni_extra = pvlib.irradiance.get_extra_radiation(times)
  fig, axes = plt.subplots(ncols=2, nrows=2, sharex=True, sharey=True, squeeze=True)
  axes = axes.flatten()
  plt.rcParams['axes.grid'] = True # Global setting grid for all subplots
  for (aod, pw), ax in zip(itertools.chain(itertools.product(aod700, precipitable_water)), axes):
    cs = pvlib.clearsky.simplified_solis(apparent_elevation, aod, pw, pressure, dni_extra)
    cs.plot(ax=ax, title='aod700={}, pw={}'.format(aod, pw))
  plt.savefig('cs_compare.png', bbox_inches='tight')

def plot_solis(loc, key, apparent_elevation):
  '''
  Contour plots of irradiance as a function of both PW and AOD;
  input parameters: ghi, dni or dhi
  '''
  aod700 = np.linspace(0, 0.5, 101)
  precipitable_water = np.linspace(0, 10, 101)
  #pressure = 101325
  pressure = pvlib.atmosphere.alt2pres(loc.altitude)
  dni_extra = 1364
  aod700, precipitable_water = np.meshgrid(aod700, precipitable_water)
  # inputs are arrays, so solis is an OrderedDict
  solis = pvlib.clearsky.simplified_solis(apparent_elevation, aod700, precipitable_water, pressure, dni_extra)
  # plot contours
  n = 15
  vmin = None
  vmax = None
  irrad = solis[key]
  fig, ax = plt.subplots()
  im = ax.contour(aod700, precipitable_water, irrad[:, :], n, vmin=vmin, vmax=vmax)
  imf = ax.contourf(aod700, precipitable_water, irrad[:, :], n, vmin=vmin, vmax=vmax)
  ax.set_xlabel('AOD')
  ax.set_ylabel('Precipitable water (cm)')
  ax.clabel(im, colors='k', fmt='%.0f')
  fig.colorbar(imf, label=f'{key} (W/m**2)')
  ax.set_title(f'{key}, elevation={apparent_elevation}')
  plt.savefig(f'solis_{key}_{apparent_elevation}.png', bbox_inches='tight')

# Main

info1 = (1240, 1.2)
info2 = (550, 3.1)
#convert_aod(info1, info2)

loc = Location(-3.21, -53.823, tz='UTC', altitude=50, name='T3')
times = pd.date_range(start='2015-02-08 09:00:00', end='2015-02-08 23:00:00', freq='5min', tz=loc.tz)
clear_sky(loc, times)

aod700 = [0.01, 0.1]
precipitable_water = [0.5, 5]
#compare(loc, times, aod700, precipitable_water)

apparent_elevation = 40
#plot_solis(loc, 'ghi', apparent_elevation)