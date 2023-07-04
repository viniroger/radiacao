## Atividade 10 - Simplified Solis

Essa atividade tem como objetivo calcular valores de irradiância usando um modelo de transferência radiativa e que considere informações de vapor d'água e aerossóis. Para isso, serão considerados diferentes cenários para comparar o impacto dessas variáveis em gráficos tipo *subplot* e *contour*.

O modelo [Simplified Solis](https://pvlib-python.readthedocs.io/en/stable/user_guide/clearsky.html) (Ineichen, 2008) parametriza a irradiância em termos de água precipitável e profundidade óptica de aerossol. O modelo de céu claro de Solis é um esquema baseado em cálculos de transferência radiativa e na relação Beer-Lambert. Por ser muito custoso computacionalmente quando usado em larga escala com dados de satélite, foi criada uma versão analítica simplificada de banda larga do modelo Solis.

Os dados de água precipitável (PW) e de profundidade óptica do aerossol (AOD) podem ser obtidos de diferentes fontes. A AOD depende do comprimento de onda, e o modelo Simplified Solis requer AOD a 700 nm. Para converter AOD entre diferentes comprimentos de onda usando o expoente de Angstrom, pode-se usar as funções *angstrom_alpha()* e *angstrom_aod_at_lambda()*, desde que se tenha a medida em pelo menos dois comprimentos de onda.

1. Faça o fork do repl e rode o script main.py somente com a função "convert_aod" chamada. O que acontece comparativamente com o valor de AOD nos três comprimentos de onda analisados? Justifique sua resposta.
2. Para realizar o cálculo do modelo de céu claro, comente todas as funções deixando apenas a "clear_sky". Também altere as variáveis de localização e rode o script. Atenção para o fuso horário e intervalo temporal.
3. Para verificar o efeito do aerossol e da água precipitável, deixe descomentada apenas a função "compare" e rode o script. Analise os gráficos obtidos.
4. Para observar o efeito dessas variáveis de modo mais amplo, use a função "plot_solis" para fazer mapas de contornos. Analise o gráfico, altere o valor de elevação para 40° e rode o script novamente. Compare as duas figuras e indique a diferença no comportamento da irradiância.

### Referências

Ineichen, P. (2008). A broadband simplified version of the Solis clear sky model. Em Solar Energy (Vol. 82, Issue 8, p. 758–762). Elsevier BV. https://doi.org/10.1016/j.solener.2008.02.009