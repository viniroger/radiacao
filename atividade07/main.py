import os
import matplotlib.pyplot as plt
import calendar
import pvlib
import h5py
import pandas as pd

# Methods


def plot_turbidity_map(month, vmin=1, vmax=100):
  '''
  Plot turbidity map for a given month number
  '''
  plt.figure()
  with h5py.File(filepath, 'r') as lt_h5_file:
    ltdata = lt_h5_file['LinkeTurbidity'][:, :, month - 1]
  plt.imshow(ltdata, vmin=vmin, vmax=vmax)
  # data is in units of 20 x turbidity
  plt.title('Linke turbidity x 20, ' + calendar.month_name[month])
  plt.colorbar(shrink=0.5)
  plt.tight_layout()
  plt.savefig('turbidity_map.png', bbox_inches='tight')


def plot_timeseries(times, site):
  '''
  Plot time series from multiple times
  at a latitude/longitude point
  '''
  plt.figure()
  turbidity = pvlib.clearsky.lookup_linke_turbidity(times, site[0], site[1])
  turbidity.plot()
  plt.title(f'Linke Turbidity - {site[2]}')
  plt.ylabel('Linke Turbidity')
  plt.savefig('turbidity_ts.png', bbox_inches='tight')


# Main

# Define HDF file path
pvlib_path = os.path.dirname(os.path.abspath(pvlib.clearsky.__file__))
filepath = os.path.join(pvlib_path, 'data', 'LinkeTurbidities.h5')

# Define times and lat/lon site
times = pd.date_range(start='2014-01-01', end='2016-01-01', freq='1D')
site = (-3.21, -60.6, 'T3')

#plot_turbidity_map(1)
plot_timeseries(times, site)
