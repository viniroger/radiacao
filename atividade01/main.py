# Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#from metpy.units import units

print('Atividade 1 - Lei de Planck')


def blackbody_radiation(temperature, wmin=0.01e-6, wmax=2e-6, nsteps=100):
  h = 6.626*10**(-34) # Js
  k = 1.381*10**(-23) # J/K
  c = 2.998e8 # m/s
  wavelength = np.linspace(wmin, wmax, nsteps)
  radiation = 2*h*c**2/((wavelength**(5))*(np.exp(h*c/(wavelength*k*temperature))-1))
  return wavelength, radiation


w, r = blackbody_radiation(5000)
plt.plot(w, r)
# Exibir a imagem (janela/output/corpo)
#plt.show()
# Salvar imagem em arquivo
plt.savefig('blackbody.png', bbox_inches='tight')
