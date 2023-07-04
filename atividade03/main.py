# Importar bibliotecas
import os
import itertools
import matplotlib.pyplot as plt
import pandas as pd
from pvlib.location import Location

# Inserir latitude e longitude do lugar
loc = Location(-3.21, -53.823, tz='UTC', altitude=50, name='T3')
#loc = Location(-3.21, -53.823, tz='America/Manaus', altitude=50, name='T3')
times = pd.date_range(start='2015-02-08 09:00:00', end='2015-02-08 23:00:00', freq='5min', tz=loc.tz)
#times = pd.date_range(start='2015-02-08 05:00:00', end='2015-02-08 18:00:00', freq='5min', tz=loc.tz)
day_str = times[0].strftime('%Y-%m-%d')
# Obter céu claro usando Ineichen com climatologia por padrão
cs = loc.get_clearsky(times)

# Extra - ver tipo de variável e salvar CSV com dados
#print(type(cs))
#cs.to_csv('cs.csv')

cs.plot(linestyle=':', marker='o')
plt.ylabel('Irradiancia $W/m^2$')
plt.title(f'Ineichen climatological turbidity - {day_str}')
#plt.show()
plt.savefig('cs.png', bbox_inches='tight')