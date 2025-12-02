## Objetivo da aula

Utilizar da linguagem DAX para fazer criação de Colunas, medidas e fazer tratamentos iniciais de dados

## Tópicos

- DAX

- Normalização de dados

- Measures

- Colunas

## Metodologia e sugestões

Comece a aula falando sobre o DAX, explique como a linguagem funciona, mostre a documentação. Enfatise que não será possível falar de todos os comandos, mas cobriremos vários úteis

Abra e explore o dataset da copa do mundo, nele, você poderá ver que há uma quantidade MUITO robusta de dados, mas que os dados estão, em geral, separados por time, o que inviabiliza analises de conjunto.

Proponha que se avalie se essa copa do mundo está acima ou abaixo da média de cartões amarelos da copa anterior. Para resolver, crie uma coluna para cartoes amarelos totais e compare com a média anterior. Você pode criar uma measure também, para fazer essa validação ser iterativa ao longo da copa (considerando que os jogos ainda estivessem acontecendo).

Mostre como utilizar as measures no Gauge, fazendo por exemplo uma measure que seja a quantidade de cartoes amarelos esperados considerando o total de jogos corridos.

## Arquivos complementares

Esse dataset da copa do mundo é bastante interessante e tem grande volume de dados, ele serve tanto para o exercício quanto para as demonstrações