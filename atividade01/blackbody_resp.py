# Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#from metpy.units import units

print('Atividade 1 resposta - Lei de Planck')

def blackbody_radiation(temperature, wmin=0.01e-6, wmax=2e-6, nsteps=100):
  h = 6.626*10**(-34) # Js
  k = 1.381*10**(-23) # J/K
  c = 2.998e8 # m/s
  wavelength = np.linspace(wmin, wmax, nsteps)
  radiation = 2*h*c**2/((wavelength**(5))*(np.exp(h*c/(wavelength*k*temperature))-1))
  return wavelength, radiation

#w, r = blackbody_radiation(5000)
#plt.plot(w, r)
#plt.xlabel('Comprimento de onda ($\mu m$)')
#W/m2srum
#plt.ylabel('Radiância espectral ($Wm^{-2}sr^{-1} \mu m^{-1}$)')
# Exibir a imagem (janela/output/corpo)
#plt.show()
# Salvar imagem em arquivo
#plt.savefig('blackbody.png', bbox_inches='tight')

fig, ax = plt.subplots()
# ZIP - array com itens emparelhados
for l, c in zip([5000, 6000, 7000], ['#a6611a', '#80cdc1', '#018571']):
  w, r = blackbody_radiation(l)
  ax.plot(w/1e-6, r/1e6, label=str(l)+' K', color=c)
  plt.xlabel('Comprimento de onda ($\mu m$)')
  plt.ylabel('Radiância espectral ($Wm^{-2}sr^{-1} \mu m^{-1}$)')
plt.legend()
plt.title('Lei de PLanck')
plt.savefig('blackbody_2.png', bbox_inches='tight')

# Base: https://www.youtube.com/watch?v=FdGfPX43gBM