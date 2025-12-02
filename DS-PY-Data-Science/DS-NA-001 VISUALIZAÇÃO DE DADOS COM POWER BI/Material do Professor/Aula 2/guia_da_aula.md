## Objetivo da aula

Apresentar as visualizações Card e Gauge, possibilitar filtragens simples via Slicer e também comentar sobre como as tabelas se relacionam no Power BI e os benefícios gerados por esses relacionamentos

## Tópicos

- Visualização Card
- Agregações de dados
- Slicer
- Relacionamento entre tabelas
- Visualização Gauge


## Metodologia e sugestões

O problema gerador dessa aula é o funcionamento de telas de metas. Vale abrir o google junto com os alunos e buscar algumas telas de metas para que eles tenham uma referencia visual. A partir daí uma linha narrativa sugerida é escolher um dataset (aqui sugiro o disney_movies_gross_tratado) e ir evoluindo a construção dessa tela.

Primeiro, mostrando um card, será possível mostrar o total da receita gerada pelos filmes, aproveite para explicar os tipos de agregações de dados que são possíveis no Power BI

Em seguida, será possível ver a receita por genero de filme.

Depois, utilizando o relacionamento entre tabelas, é possível agregar tabelas diferentes e fazer o slicing por diretor, por exemplo.

Por fim, pode-se usar a visualização Gauge para que se visualize quais diretores bateram a meta.

Exercício: Peça aos alunos que discutam quanto é uma meta razoável de receita para que a disney bata até 2020. Instrua-os a construirem essa visualização usando o dataset disney_revenue. Por fim, peça que eles adicionem as linhas faltantes até 2020, atualizem o dash e vejam se a meta foi batida.

## Arquivos complementares

Os csvs se referem a filmes da disney. Podem ser usados para demonstrar tanto o Gauge quanto o relacionamento entre tabelas

-----

1. Relacionamentos no power BI
Subir os dados do dataset Disney no power BI. Em seguida, conectar as datasets de directors, movies e characters. Trabalhe com os alunos para eles saberem qual chave que conecta essas tabelas. E em seguida mostre como conectar essas tabelas.

1. Relembrar a criação de cards e gauges.

Criar cards e gauges
* Cards: Total Revenue, Avg Revenue e Max Revenue
* Cards: Total Movies, Total directors e Total Characters
* Gauge: Total Revenue with target 40B target

1. Segmentação de dados: slicer
Vamos criar uma segmentação de dados com base no filme, tipo de filme e diretores.

* Slicer: Por filme e por diretor

Mostrar a relação de interação entre filtros e elementos visuais. Tirar a interação de cards totais e manter os cards de valor específico.