## Atividade 1 - Lei de Planck

Um corpo negro é um objeto teórico que absorve toda a radiação incidente sobre ele e emite radiação de forma isotrópica, ou seja, da mesma forma em todas as direções. A Lei de Planck descreve a distribuição espectral de energia radiante emitida por um corpo negro em equilíbrio térmico. Ela pode ser expressa em termos da densidade espectral de energia radiante (energia radiante emitida por unidade de tempo, por unidade de área de superfície e por unidade de comprimento de onda) pela fórmula:

$$B(\lambda,T) = \frac{2hc^2}{\lambda^5[exp(hc/\lambda kT)-1]}$$

A radiação de corpo negro possui um espectro contínuo que depende apenas de sua temperatura. Quanto maior a temperatura, maior a intensidade da radiação emitida, com o pico se deslocando para comprimentos de onda menores.

A **MetPy** é uma biblioteca de ferramentas em Python para ler, visualizar e realizar cálculos com dados meteorológicos. As variáveis numéricas podem vir acompanhadas da informação de unidade de medida (*units*), facilitando a manipulação de valores no código.

1. Faça o fork do repl, rode o script da atividade e verifique se a figura foi gerada;
2. Atualize o código para incluir informações nos eixos e criar curvas (*subplots*, com legenda) no mesmo gráfico para três temperaturas: 5000, 6000 e 7000 K;
3. Analise o gráfico gerado e explique as diferenças nas curvas obtidas.

Extra: [simulador do Espectro de Corpo Negro](https://phet.colorado.edu/pt_BR/simulations/blackbody-spectrum)