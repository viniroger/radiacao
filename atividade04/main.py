import numpy as np
import matplotlib.pyplot as plt
import imageio
from py_sky import set_scene, render, show

width = 32
height = 32

images = list()

for i, zenith in enumerate(np.arange(0, 101, 5)):
    scene = set_scene(zenith=zenith, azimuth=180, width=width, height=height)
    
    rgb = render(scene)
    
    filename = 'sky_' + str(i).zfill(2) + '.png'
    imageio.imwrite(filename, rgb)
    
    images.append(imageio.imread(filename))
tmp = images.copy()
tmp.reverse()
imageio.mimsave('movie.gif', images + tmp, fps=60, duration=0.1)