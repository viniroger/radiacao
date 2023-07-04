# Importar bibliotecas
import os
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import pvlib
from pvlib.location import Location

# Inserir latitude e longitude do lugar
loc = Location(-3.21, -53.823, tz='UTC', altitude=50, name='T3')

times = pd.date_range('2014-01-01', '2015-12-31', freq='1M')
extra = pd.Series(pvlib.irradiance.get_extra_radiation(times, method='spencer'), times)

extra.plot(linestyle=':', marker='o')
plt.ylabel('Extraterrestrial radiation $W/m^2$')
#plt.show()
plt.savefig('extraterrestrial_radiation_monthly.png', bbox_inches='tight')