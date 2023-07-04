## Atividade 7 - Linke Turbidity

O objetivo dessa atividade é fazer mapas de turbidez de Linke usando leitura de dados HDF e extraindo dados pontuais para gerar uma série temporal dessa variável. Com isso, será possível a comparação de valores de turbidez climatológica em diferentes lugares e épocas do ano.

O modelo de céu claro de Ineichen & Perez (2002) parametriza a irradiância em termos da turbidez de Linke (Linke, 1922). O coeficiente Linke turbidity tem a vantagem de ser amplamente utilizado desde 1922 para quantificar esta informação, mas tem a desvantagem de ser dependente da massa de ar. 

O trabalho de Ineichen & Perez (2002) propõem uma nova formulação para o coeficiente Linke turbidity com o objetivo de minimizar sua dependência da geometria solar.

A biblioteca *pvlib* inclui um arquivo com valores mensais de [turbidez climatológica](https://pvlib-python.readthedocs.io/en/stable/user_guide/clearsky.html#ineichen-and-perez) para o globo. Esse arquivo está no formato H5, que é um arquivo de dados salvo no Hierarchical Data Format (HDF), muito usado em ciências da Terra. Ele contém matrizes multidimensionais de dados científicos e pode ser manipulado usando a biblioteca *h5py*.

1. Façar o fork da atividade e rode o script principal para verificar a imagem gerada. Quais regiões apresentam maior turbidez? Por quê?
2. Cada aluno deve alterar o parâmetro de entrada para um mês diferente e rodar novamente o script. Aponte as diferenças em cada mapa e busque possíveis explicações para elas.

A função *lookup_linke_turbidity()* recebe uma data, latitude e longitude e retorna o valor de turbidez climatológica correspondente. Por padrão, a função interpola linearmente a turbidez mês a mês, assumindo que os dados brutos são válidos no dia 15 de cada mês.

3. Comente a chamada do método que gera o mapa e descomente a chamada do método que gera séries temporais de turbidez para um determinado ponto. Altere as coordenadas desse ponto para seu local de estudo e rode o script.
4. Analise o gráfico gerado na imagem e informe quais meses apresentam maiores e menores valores para comparação com os colegas.
5. Compare o seu resultado com o gráfico gerado na atividade anterior, com dados da AERONET e analise as semelhanças e diferenças.

A função *kasten96_lt()* pode ser usada para calcular a turbidez de Linke (Kasten, 1996), o que requer água precipitável e profundidade óptica de aerossol (AOD).

### Referências

P. Ineichen and R. Perez, “A New airmass independent formulation for the Linke turbidity coefficient”, Solar Energy, 73, pp. 151-157, 2002.

F. Kasten, “The linke turbidity factor based on improved values of the integral Rayleigh optical thickness,” Sol. Energy, vol. 56, no. 3, pp. 239–244, Mar. 1996.

F. Linke, “Transmissions-Koeffizient und Trubungsfaktor”, Beitrage zur Physik der Atmosphare, Vol 10, pp. 91-103 (1922)
