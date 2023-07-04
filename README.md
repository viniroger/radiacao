# Atividades práticas - Meteorologia Física 2

Esse documento trata das atividades práticas de python na disciplina [ACA0326](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=ACA0326&codcur=14010&codhab=1) - Meteorologia Física 2 (IAG/USP) 2023. Essas atividades tem como objetivos: trabalhar conceitos de radiação atmosférica através de exemplos numéricos; praticar a programação em python. O trabalho foi implementado originalmente no Replit, mas esse código pode ser todo importado nessa plataforma diretamento do Github da seguinte forma:

1. Acesse sua área restrita ao realizar o login;
2. Clique em "+ Create Repl" e selecione o botão "Import from GitHub";
3. Escreva a URL no respectivo campo: github/viniroger/radiacao;
4. Clique no botão "Import from GitHub" e aguarde.

Originalmente, foi feito um repl para cada atividade (radiacao1, radiacao2, etc), mas isso exige instalar praticamente os mesmos pacotes diversas vezes. A sugestão é usar um repl só para todas as atividades, ou trabalhar localmente mesmo clonando o projeto para um computador.

## Atividade 0 - Ambiente de trabalho

A programação será realizada usando o [Replit](https://replit.com/): uma plataforma online e gratuita que permite a programação em diversas linguagens e frameworks. Com isso, os usuários podem escrever e executar código diretamente em um navegador web, sem precisar instalar ou configurar um ambiente de desenvolvimento em sua própria máquina. Também possui recursos de colaboração em tempo real, integrações com serviços de versionamento, etc.

Seu uso é feito através de login em uma conta onde serão guardados os códigos, outros arquivos e configurações em projetos (chamados "repl"). Para ter acesso ao projeto e fazer uso dos códigos no Replit, crie uma conta, acesse o link do projeto e clique em *fork*. Um *fork* (bifurcação/ramificação) é quando um desenvolvedor inicia um projeto independente com base no código de um projeto já existente - veja mais sobre versionamento de código nos posts [Github](https://www.monolitonimbus.com.br/github/) e [Bitbucket](https://www.monolitonimbus.com.br/bitbucket-configuracao-e-branches/). Você também pode clicar em *show code* e copiar os scripts para rodar localmente.

Ao entrar na *cover page* do repl, clique em *show code* e selecione o arquivo index.md na lista que surgirá à esquerda. A documentação está em *Markdown*: um formato de simples de marcação de texto. A ideia é marcar um texto informando o que é importante, como um tópico, links e imagens, sem a necessidade de utilizar marcações mais complexas, como o HTML.

Os códigos utilizados nas atividades estão em python. O **python** é uma linguagem de programação muito usada nos mais diversos segmentos, que prioriza a legibilidade. Para aumentar seus recursos, é possível instalar bibliotecas para cada tarefa. Com o Replit, as bibliotecas são instaladas na nuvem na primeira vez que é importado no código e as informações são guardadas nos "packager files". Algumas das usadas aqui são comuns em diversos projetos: numpy (funções matemáticas), pandas (dados) e matplotlib (gráficos).

- [Dicas de estudo de programação](https://www.monolitonimbus.com.br/dicas-de-estudo-de-programacao/) ; [Gráficos em python](https://www.monolitonimbus.com.br/graficos-em-python/)

RESUMO DE PROCEDIMENTOS PARA AS AULAS

1. Alunos devem fazer login no site do replit (https://replit.com/) enquanto instrutor abre repl referente à atividade do dia em sua conta;
2. Caso tenha exercícios a serem revisados da atividade anterior, os alunos devem acessar o repl dessa atividade em sua própria conta (fork já foi feito na última aula) - para comparar códigos e figuras, o monitor pode abrir a *cover page* da atividade e selecionar o fork do aluno na lista de forks da atividade;
3. Para uma nova atividade, os alunos devem digitar no navegador o link da aula (https://replit.com/@viniroger/radiacao3, por exemplo) e fazer o fork para trabalharem nos próprios ambientes - monitor pode abrir aba anônima para mostar *cover page* e ficar com a mesma tela que os alunos.

## Lista de atividades

A atividades foram programadas para durarem de 30 a 40 minutos:

- 1 LEI DE PLANCK - [atividade01](https://github.com/viniroger/radiacao/blob/master/atividade01/index.md)
- 2 POSIÇÃO DO SOL NO CÉU - [atividade02](https://github.com/viniroger/radiacao/blob/master/atividade02/index.md)
- 3 IRRADIÂNCIA DE CÉU CLARO  - [atividade03](https://github.com/viniroger/radiacao/blob/master/atividade03/index.md)
- 4 POLARIZAÇÃO DO CÉU - [atividade04](https://github.com/viniroger/radiacao/blob/master/atividade04/index.md)
- 5 NUVENS E SEGMENTAÇÃO DE IMAGENS - [atividade05](https://github.com/viniroger/radiacao/blob/master/atividade05/index.md)
- 6 AERONET - [atividade06](https://github.com/viniroger/radiacao/blob/master/atividade06/index.md)
- 7 LINKE TURBIDITY - [atividade07](https://github.com/viniroger/radiacao/blob/master/atividade07/index.md)
- 8 RADIAÇÃO SOLAR EM SUPERFÍCIE INCLINADA - [atividade08](https://github.com/viniroger/radiacao/blob/master/atividade08/index.md)
- 9 SIMULAÇÃO DE SISTEMA PV - [atividade09](https://github.com/viniroger/radiacao/blob/master/atividade09/index.md)
- 10 SIMPLIFIED SOLIS - [atividade10](https://github.com/viniroger/radiacao/blob/master/atividade10/index.md)
- 11 MODELO DE TRANSFERÊNCIA RADIATIVA E COMENTÁRIOS DA AVALIAÇÃO - [atividade11](https://github.com/viniroger/radiacao/blob/master/atividade11/index.md)

Obs. 1: Seminário [Variabilidade do recurso solar](https://www.monolitonimbus.com.br/palestra-sobre-variabilidade-do-recurso-solar-na-usp/) dado para complementar as atividades práticas com um pouco mais de teoria.

Obs. 2: A atividade de avaliação (arquivo avaliacao.odt) deve ser feita pelos alunos, entregue e corrigida pelo instrutor antes da última atividade, quando serão discutidos os resultados.

## Tabela com informações dos locais de estudo

|       Nome do local      | Latitude | Longitude | Altitude | Fuso horário      |  Responsável  |
|:------------------------:|:--------:|:---------:|:--------:|-------------------|:-------------:|
| T3, MAN                  | -3.21    | -60.600   | 50       | America/Manaus    | instrutor     |
| Brasília, BRB            | -15.601  | -47.713   | 995      | America/Sao_Paulo | aluno1        |
| Petrolina, PTR           | -9.069   | -40.320   | 380      | America/Recife    | aluno2        |
| São Martinho, SMS        | -29.443  | -53.823   | 475      | America/Sao_Paulo | aluno3        |
| São Paulo, IAG           | -23.560  | -46.734   | 754      | America/Sao_Paulo | aluno4        |
| Almeria, ESP             | 37.093   | -2.381    | 500      | Europe/Madrid     | aluno5        |
| São Tomé e Príncipe, STP | 0.000    | 6.520     | 34       | Africa/Sao_Tome   | aluno6        |
| Alasca, EUA              | 61.585   | -149.779  | 65       | America/Anchorage | aluno7        |
| Rajastão, IND            | 27.518   | 71.928    | 200      | Asia/Kolkata      | aluno8        |
| Qinghai, CHI             | 36.406   | 94.886    | 2815     | Asia/Shanghai     | aluno9        |
| EACF, ANT                | -62.085  | -58.388   | 5        | Antarctica/Palmer | aluno10       |
| Werneuchen, ALE          | 52.652   | 13.691    | 80       | Europe/Berlin     | aluno11       |
| Darlington, AUS          | -34.647  | 146.033   | 125      | Australia/Sydney  | aluno12       |
| Toquio, JAP              | 35.69    | 139.69    | 40       | Asia/Tokyo        | aluno13       |

[Mapa dos locais de estudo no Google My Maps](https://www.google.com/maps/d/u/0/edit?mid=1UBtPafntKX5PEOZBX0mwy6VoaRs8_4g&usp=sharing)
