# Projetos URI

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0014433  |  Maria Luiza Ferreira |
| 15/0009313  |  Felipe Hargreaves |

## Sobre

#### Contaminação 
Estamos no ano 2241, e a colonização de outros planetas já é uma realidade. Você trabalha no centro de controle de recursos, no planeta URI-942, controlando principalmente os estoques de água. A água é armazenada em tanques subterrâneos, protegida das altas temperaturas da superfície.

Porém, seus colegas Márcio e Ana descobriram falhas nas paredes de alguns tanques, o que pode levar a contaminação do estoque de água. Seus colegas conseguiram identificar os pontos com falhas onde pode haver a infiltração de contaminantes. Sabendo que os agentes contaminantes se espalham por todo o tanque de água afetado, sua tarefa é estimar a contaminação da água de acordo com os mapas fornecidos por seus colegas.

Os mapas foram discretizados em células, sendo que as células podem corresponder a uma região com rocha, água (tanque) ou agente contaminante. Devido as rachaduras, uma célula com agente contaminante contamina as células adjacentes (esquerda, direita, acima e abaixo) contendo água, porém a contaminação é barrada por células de rocha.

Problema retirado do URI: https://www.urionlinejudge.com.br/judge/pt/problems/view/1583


#### Classificação do Problema

A solução para o problema envolveu os conceitos de grafos ao aplicar uma adaptação do Breadth-First Search (BFS), funcionando de forma similar ao _flood fill_.

## Screenshots

![Log de resposta aceita no URI](img/ac.jpg)

## Instalação 
**Linguagem**: Python<br>
**Execução**: Dentro da pasta do projeto, executar `python contaminacao.py` e inserir entradas de acordo com os exemplos abaixo. Para encerrar a execução, inserir um caso de teste com as entradas `0 0`.


## Uso 
#### Contaminação 
A entrada é composta por vários mapas, sendo que a descrição de cada mapa começa com uma linha contendo dois inteiros N e M, correspondente ao número de linhas e de colunas do mapa. As N linhas a seguir descrevem o mapa, cada linha contendo M caracteres, além do pulo de linha. Os caracteres possíveis são: A, que representa uma célula contendo água, X, que representa uma célula com rocha e T que representa uma célula com agente contaminante.

A entrada termina quando N = M = 0, caso que não deve ser processado. Em todos os mapas, N e M são menores ou iguais a 50.

Exemplo de entradas e saídas:
| Entrada | Saída | 
|---|---|
| 6 7 <br> XXAAXXX <br> XXAAXAX <br>  XXXXAXX <br> XAAAAAX <br> TAAXAAA <br> XXXXXXX |  XXAAXXX <br> XXAAXAX <br> XXXXTXX <br> XTTTTTX <br> TTTXTTT <br> XXXXXXX|
| 3 3 <br> TTT <br> XXX <br> AAA | TTT <br> XXX <br> AAA|

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




