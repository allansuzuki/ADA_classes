# Primeiros passos no Power BI
 
Dando sequência em como utilizar a ferramenta Power BI para a visualização de dados. Daremos os primeiros passos para construir as visualizações. Primeiramente um entendimento de como as tabelas se relacionam dentro do Power BI, em seguida, as visualizações dos tipos Card e Gauge e alguns detalhes sobre cada uma delas.
 
## Relacionamentos no Power BI
 
Quando trabalhamos com uma base de dados que possui várias tabelas, elas vão estar relacionadas por meio das chaves primárias e estrangeiras de cada tabela.
 
Sendo assim, o Power BI precisa reconhecer esses relacionamentos para cruzar as informações relacionadas nas visualizações dos dashboards.
 
Confere na **Figura 1** a conexão com uma base de dados com várias tabelas, é possível selecionar apenas as tabelas necessárias para a criação das visualizações, na figura foram selecionadas todas as tabelas.
 
| ![Base de dados com várias tabelas](https://s3-sa-east-1.amazonaws.com/lcpi/d327fbfa-ceb0-4e46-89f7-a5af107c720e.png) |
|:--:|
| **Figura 1** – _Base de dados com várias tabelas_ (Fonte da imagem: do autor) |
 
Após os dados carregados, teremos todos os campos das tabelas selecionadas como pode ver na **Figura 2**. É possível utilizar todos esses campos e aproveitar o relacionamento entre eles para cruzar informações entre essas tabelas, assim enriquecendo as visualizações.
 
| ![Campos das tabelas no Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/5258e672-76a0-41c3-90e7-4666fc5a494e.png) |
|:--:|
| **Figura 2** – _Campos das tabelas no Power BI_ (Fonte da imagem: do autor) |
 
Mas onde que esses dados estão se relacionando? A **Figura 3**, mostra exatamente todas as tabelas carregadas e os relacionamentos de cada uma. Em destaque o relacionamento entre a tabela florestas e a tabela municípios através da coluna id_municipio. Ao clicar na linha que indica o relacionamento, o Power BI exibe exatamente as colunas que formam esse relacionamento, deixando em destaque.
 
| ![Relacionamentos no Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/4be58e90-9ecb-4229-b9e0-45acd1c6a0f5.png) |
|:--:|
| **Figura 3** – _Relacionamentos no Power BI_ (Fonte da imagem: do autor) |
 
Agora que já entendemos como as tabelas se relacionam após a carga dos dados, podemos construir as primeiras visualizações. Agora conheceremos os tipos de visualizações card e gauge.
 
## Visualização Card
 
A visualização do tipo card, também conhecida como cartão ou big number, é utilizada para mostrar números importantes do negócio e normalmente estão na parte superior do dashboard.
 
Para selecionar o cartão, escolhemos o tipo de gráfico no menu de visualizações, ele é o visual em destaque na **Figura 4**.
 
| ![Visualizações](https://s3-sa-east-1.amazonaws.com/lcpi/5ca62e26-c622-445d-969f-86dbb61da0c8.png) |
|:--:|
| **Figura 4** – _Visualizações_ (Fonte da imagem: do autor) |
 
Após selecionar o visual, é preciso selecionar o campo que será utilizado para exibir no cartão. Observe os itens em destaque na **Figura 5**. Em **vermelho** está a seleção do visual e o campo que foi selecionado para exibir o dado no cartão, tudo isso no menu de visualizações. Já a seleção em **verde** no menu de campos, é onde temos todos os campos disponíveis e que foi selecionado para o visual ficar marcado no checkbox. E finalizamos com a seleção **rosa**, onde o cartão já é exibido na área do dashboard.
 
| ![Card no Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/25afcf0d-04ab-4656-bc4a-39e9ff54e373.png) |
|:--:|
| **Figura 5** – _Card no Power BI_ (Fonte da imagem: do autor) |
 
A formatação é conforme o tipo do gráfico selecionado. Ainda no menu de visualização podemos formatar o visual do gráfico, assim, temos uma grande variedade de opções para deixar mais elegantes o gráfico no dashboard. A **Figura 6** mostra exatamente onde acessar para modificar o visual dos gráficos.
 
| ![Formatação Visual](https://s3-sa-east-1.amazonaws.com/lcpi/8ed21049-f631-4b77-8a88-879ff9538690.png) |
|:--:|
| **Figura 6** – _Formatação Visual_ (Fonte da imagem: do autor) |
 
Também é possível alterar algumas configurações gerais do gráfico, essas estarão presentes em todos os gráficos, como título, efeitos entre outras. Para alterar as configurações gerais é só seguir os passos da **Figura 7**.
 
| ![Formatação Geral](https://s3-sa-east-1.amazonaws.com/lcpi/4b1802f3-48fd-45c9-a2ec-7b588ef679a4.png) |
|:--:|
| **Figura 7** – _Formatação Geral_ (Fonte da imagem: do autor) |
 
Agora precisamos relembrar alguns conceitos. As agregações são uma forma de agrupar os dados conforme a necessidade da exibição da informação. Dessa forma, selecionamos os registros individuais linha a linha e agregamos em um só número, podendo ser uma soma, uma média, o valor máximo ou mínimo, entre outras opções. A **Figura 8** mostra como verificar a agregação aplicada e alterá-la caso necessário.
 
| ![Agregações](https://s3-sa-east-1.amazonaws.com/lcpi/cb180a17-4d83-42ce-9330-8f234f5802d9.png) |
|:--:|
| **Figura 8** – _Agregações_ (Fonte da imagem: do autor) |
 
Para finalizar o cartão, faremos uma alteração no texto exibido para melhor entendimento da informação apresentada. Lembrando que o cartão é uma informação de destaque e precisa estar o mais claro possível. Na **Figura 9** observe como selecionar a opção **Renomear para este visual**, assim, alteramos o nome do campo apenas para esse gráfico e podemos deixar a informação mais clara para o usuário final.
 
| ![Renomeando Card](https://s3-sa-east-1.amazonaws.com/lcpi/b508d125-16f8-4bf9-a0b2-5cafc644c536.png) |
|:--:|
| **Figura 9** – _Renomeando Card_ (Fonte da imagem: do autor) |
 
Agora chegamos ao objetivo de apresentar o cartão no dashboard, confere a **Figura 10**.
 
| ![Card](https://s3-sa-east-1.amazonaws.com/lcpi/9cb48f3c-5b93-40ac-8612-eec146d4c0d6.png) |
|:--:|
| **Figura 10** – _Card_ (Fonte da imagem: do autor) |
 
### Quando utilizar a visualização de card
*   Indicadores importantes que podem ser representados com apenas um número ou percentual
*   Números relevantes para o negócio que merecem destaque
 
## Visualização Gauge
 
A visualização do tipo gauge, também conhecida como indicador, é utilizada para acompanhar valores no dashboard.
 
Para selecionar o indicador, escolhemos o tipo de gráfico no menu de visualizações, ele é o visual em destaque na **Figura 11**.
 
| ![Visualizações](https://s3-sa-east-1.amazonaws.com/lcpi/4fe45fed-52fc-4d4f-bf20-63fd5558c95b.png) |
|:--:|
| **Figura 11** – _Visualizações_ (Fonte da imagem: do autor) |
 
Após selecionar o visual, é preciso selecionar o campo que será utilizado para exibir no indicador. Observe os itens em destaque na **Figura 12**. Em **vermelho** está a seleção do visual e o campo que foi selecionado para exibir o dado no indicador, tudo isso no menu de visualizações. Já a seleção em **verde** no menu de campos, é onde temos todos os campos disponíveis e que foi selecionado para o visual ficar marcado no checkbox. E finalizamos com a seleção **rosa**, onde o indicador já é exibido na área do dashboard.
 
 
| ![Gauge no Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/b4db61f3-97ee-4242-b84e-7e0c041ed4c7.png) |
|:--:|
| **Figura 12** – _Gauge no Power BI_ (Fonte da imagem: do autor) |
 
Já vimos que a formatação é conforme o tipo do gráfico selecionado, então teremos mais algumas configurações para o tipo indicador. No menu de visualização podemos formatar o visual do gráfico e a **Figura 13** mostra exatamente onde acessar para modificar o visual dos gráficos.
 
 
| ![Formatação Visual](https://s3-sa-east-1.amazonaws.com/lcpi/16ddf05c-a455-48ce-9bce-53b8cda14ad1.png) |
|:--:|
| **Figura 13** – _Formatação Visual_ (Fonte da imagem: do autor) |
 
Temos também as configurações gerais do gráfico, essas já sabemos, estarão presentes em todos os gráficos. Para alterar as configurações gerais é só seguir os passos da **Figura 14**.
 
 
| ![Formatação Geral](https://s3-sa-east-1.amazonaws.com/lcpi/dddeabaf-cb57-4b03-8f2f-896355284a88.png) |
|:--:|
| **Figura 14** – _Formatação Geral_ (Fonte da imagem: do autor) |
 
Já relembramos o que são as agregações dos dados. A **Figura 15** mostra mais uma vez como verificar a agregação aplicada e alterá-la caso necessário.
 
 
| ![Agregações](https://s3-sa-east-1.amazonaws.com/lcpi/c88c3f95-4635-4b69-9613-1d8e0f5e9265.png) |
|:--:|
| **Figura 15** – _Agregações_ (Fonte da imagem: do autor) |
 
Para finalizar o indicador, faremos uma alteração nos valores do eixo e objetivo. Lembrando que o indicador é uma visualização para acompanhar metas e KPIs, então é preciso que as informações estejam presentes no visual. Na **Figura 16** observe como selecionar a opção **Eixo do medidor**, assim, alteramos os valores mínimo, máximo e destino e podemos deixar o acompanhamento do indicador muito mais efetivo.
 
 
| ![Formatando Eixos](https://s3-sa-east-1.amazonaws.com/lcpi/6acca04f-3221-4389-b4a5-3d540222614a.png) |
|:--:|
| **Figura 16** – _Formatando Eixos_ (Fonte da imagem: do autor) |
 
Agora chegamos ao objetivo de apresentar o indicador no dashboard, confere a **Figura 17**, com todos os detalhes do eixo ajustados anteriormente.
 
| ![Gauge](https://s3-sa-east-1.amazonaws.com/lcpi/2d485763-79ac-4c03-a1f1-d65abc8816fa.png) |
|:--:|
| **Figura 17** – _Gauge_ (Fonte da imagem: do autor) |
 
### Quando utilizar a visualização de gauge
*   Ter no dashboard indicadores claros e fáceis de interpretar
*   Indicadores para medir performance
*   Acompanhar metas ou KPIs
 
Pronto! Já foi mostrado os relacionamentos das tabelas dentro do Power BI e criadas as primeiras visualizações.
 
No próximo tópico será mostrado como aplicar filtros nas visualizações.
 
## Referências
 
*  https://docs.microsoft.com/pt-br/power-bi/
