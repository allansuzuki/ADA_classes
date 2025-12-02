## Objetivo da aula

O objetivo da primeira aula é se apresentar para os alunos, conhecê-los melhor e estabelecer alguns combinados da sua forma de dar aula.

## Tópicos

- Até onde iremos no curso
- Demonstração de um Dashboard completo
- Instalação do Power BI
- Interface do Power BI
- Conexão a fontes de dados no Power BI
- Apresentação do projeto da avaliação


## Metodologia e sugestões

Comece a aula se apresentando para os alunos, aproveite para comentar sobre sua metodologia de aula, como costuma propor exercícios e deixá-los cientes de até onde o curso vai e o que poderá ser aprendido.

**SUGESTÃO:** Geralmente está aula será ministrada no meio de um projeto maior, então pedir para os alunos se apresentarem as vezes é frustrante para eles. Uma ideia é passar um questionario do google forms com informações que você tenha intenção de saber e também curiosidades (time de futebol por exemplo). Você pode fazer uso desse forms como base de dados da demonstração prática e do exercício de exploração de dados deles.

Auxilie os alunos a instalar o Power BI, podem ocorrer dúvidas diversas da instalação e por isso é conveniente usar parte dessa aula para evitar que isso atrapalhe o desenvolvimento dos alunos.

**ALERTA:** Nesta aula, muitas vezes ocorre a descoberta de que alguns alunos estão utilizando Linux ou MacOS como sistema operacional. Neste caso existem algumas abordagens possíveis para contornar o problema, dado que o Power BI Desktop só possuí instalação para Windows. Uma delas é garantir que esse aluno esteja em grupo com alunos que tem o ferramentario disponível, outra é sugerir a instalação de uma maquina virtual. De qualquer forma, deixe claro para o aluno que os conceitos vistos no curso transcendem o Power BI e podem ser usados em outras ferramentas.

Navegue pelas abas do Power BI, mostrando conceitos e ferramentas superficialmente, comente que serão aprofundadas nas próximas aulas

Explique conexões com fontes de dados do Power BI. Quanto ao SQL, caso os alunos não tenham tido esse conteúdo antes, vale uma explicação, caso contrário, recapitule brevemente antes de demonstrar.

Deixe que eles importem alguma base de dados e então explorem a ferramenta

Por fim, apresente o projeto da disciplina. Há uma sugestão de projeto no guia geral

## Arquivos complementares

A base Northwind SQL é uma base código aberto da Microsoft e é uma boa sugestão de conjunto de dados completo para demonstrar importação de dados via SQL e relações entre tabelas

----

## Aula 1 - conexão de dados + Interface Power BI + Cards e Gauges

1. Exemplos de power BI
abra e compartilhe o link https://zoomcharts.com/en/microsoft-power-bi-custom-visuals/dashboard-and-report-examples/ para visualizar exemplos de dashboards completos.
Gosto do dashboard `power-bi-service-desk-dashboard-by-iris-mejuto-crego` porque é simples, intuitivo e bem didático.

1. Conexões com bases SQL e Excel
Partilhe com os alunos a pasta dentro do material do aluno `datasets`
Utilize a base de dados Northwind SQL pára demonstrar que é possível fazer conexões tanto com o Microsoft SQL management Studio ou com o postgreSQL e muitos outros.

1. Relacionamentos e Transformação de dados
Utilize o botão "selecionar tabelas relacionadas". Isso vai ser usado mais para frente
Mostre também o poder da ferramenta de conseguir tratar e transformar os dados. Sempre trazendo a visão de que isso vai ser visto mais a fundo em aulas à frente

1. Interface do power BI
Em seguida, após carregar os dados, mostre na aba esquerda onde fica localizado as tabelas e seus relacionamentos. Daí por diante, mostre toda a interface do Power bi desde edição das páginas, ferramentas, elementos visuais, tabelas, relacionamentos, conexões, etc...

NOTA:Pode fazer fazer todos os passos acima com base nos dados da aula 2 o disney dataset.

1. Primeiros elementos visuais: cards
Mostra que é possível adicionar os elementos a página de 3 maneiras:

* Arrastando/clicando no elemento visual
* Arrastando/clicando na medida que quer visualizar

Em seguida, adicione um `card` mostre as abas de propriedade dos elementos. Mostre limites, alterar tamanho, posição, formatação, etc... (**ATENÇÃO!** Diferentes power BI trazem diferentes textos e posições).

Introduza a ideia de criar uma medida com base em uma coluna. Explique que essa é uma boa prática e que não é preciso adivinhar como é a função ou do que se trata.

Em seguida, clica na medida utilizada e mostra que é possível formatar os valores visualizados (numero inteiro, decimal, currency, etc...)

1. Primeiros elementos visuais: Guage
Semelhantemente agora adicione o gauge trazendo uma noção de alcance de meta. Mostre que cada elemento tem teus parametros obrigatórios para funcionar.

Mostre que é possivel alterar forma, posição, altura, etc...

