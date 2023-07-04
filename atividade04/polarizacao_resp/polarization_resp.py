import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from py_sky import set_scene, render
from pvlib import solarposition

width = 32
height = 32
images = list()

# Generate sun positions
#tz = 'America/Manaus'
#lat, lon = -3.21, -60.6
#day = '2014-10-03'
tz = 'UTC'
lat, lon = -23.560, -46.734
day = '2015-03-20'
times = pd.date_range(f'{day} 00:00:00', f'{day} 23:59:59', inclusive='left', freq='H', tz=tz)
solpos = solarposition.get_solarposition(times, lat, lon)
solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]

# Loop for each sun position
for i in range(0,solpos.azimuth.size):
  zenith = solpos.apparent_zenith[i]
  azimuth = solpos.azimuth[i] - 90 # rotate 90° (N)
  print(f'Zenith={zenith} ; Azimuth={azimuth}')
  # Create image
  scene = set_scene(zenith=zenith, azimuth=azimuth, width=width, height=height)
  # Render image
  rgb = render(scene)
  # Save image
  filename = 'sky_' + str(i).zfill(2) + '.png'
  imageio.imwrite(filename, rgb)
  images.append(imageio.imread(filename))

# Create video
tmp = images.copy()
#tmp.reverse()
#images = images + tmp
imageio.mimsave('movie.gif', images, fps=60, duration=0.1)
