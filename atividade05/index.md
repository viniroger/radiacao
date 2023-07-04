## Atividade 5 - Nuvens e segmentação de imagem

O objetivo dessa atividade está em explorar uma técnica de segmentação de imagens para separar nuvem e céu claro em uma imagem. Uma imagem de céu inteiro (*All Sky Image - ASI*) contém uma visão panorâmica completa do céu a partir de um determinado ponto de observação. Normalmente, cobre uma área de 360 graus na horizontal e 180 graus na vertical. Ela pode ser feita a partir de uma câmera com lente grande angular do tipo "olho de peixe" apontada para o zênite (ponto no qual a vertical do lugar, perpendicular ao horizonte, intercepta a esfera celeste, acima do observador) ou apontada na mesma direção, porém sentido oposto, e usando um espelho esférico.

Uma etapa importante no processamento de imagens digitais para analisar o que está dentro dela é classificar seu conteúdo de pixeis em diferentes grupos. Esse processo é chamado de segmentação de imagem, cujo objetivo é transformar a representação de uma imagem em algo mais significativo e fácil de analisar. É muito comum o uso de algoritmos de agrupamento (“clusters”) para realizar esse procedimento.

O método *k-means* é um algoritmo de clusterização que busca agrupar um conjunto de dados em k clusters, onde k é um número previamente definido. O algoritmo funciona inicialmente selecionando aleatoriamente k pontos como centróides iniciais dos clusters. Em seguida, cada ponto de dados é atribuído ao centróide mais próximo, formando assim k clusters. A posição dos centróides é então atualizada para a média de todos os pontos atribuídos a ele. Este processo é repetido iterativamente até que os centróides não mudem de posição significativamente ou até que um número máximo de iterações seja atingido. O objetivo do algoritmo é minimizar a soma das distâncias euclidianas entre cada ponto de dado e o centróide de seu cluster correspondente, formando assim clusters bem definidos e separados uns dos outros.

Com o objetivo de fazer a segmentação de ASI entre céu claro e nuvens, o script faz uma separação em três classes (k = 3) usando [k-means](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html). Assim, uma classificação grosseira deve indicar se cada pixel é uma nuvem, céu claro ou interferência.

O **OpenCV** (Open Source Computer Vision Library), é uma biblioteca livre e multiplataforma para o desenvolvimento de aplicativos na área de visão computacional. Possui módulos de processamento de imagens e centenas de algoritmos, como filtros de imagem, calibração de câmera, reconhecimento de objetos, análise estrutural e outros.

1. Faça o fork do repl [radiacao5](https://replit.com/@viniroger/radiacao5), rode o script da atividade e descreva a imagem gerada;
2. Quais são os pontos positivos e negativos da classificação realizada?
3. Altere a imagem analisada e compare com as classificações com as outras imagens dos colegas.

Veja mais: [Análise de Cluster](https://www.monolitonimbus.com.br/analise-de-cluster/) e [Segmentação de imagem](https://www.monolitonimbus.com.br/segmentacao-de-imagem/)