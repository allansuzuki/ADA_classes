# Visualizações no Power BI
 
Chegou a hora de conhecer mais algumas visualizações no Power BI. As possibilidades de gráficos e as variações dos mesmos são muitas, assim devemos focar em resolver os problemas do negócio. Dessa forma conseguiremos atingir o objetivo, levar informações úteis que auxiliem na tomada de decisão.
 
A seguir duas visualizações bem importantes para acompanhar as vendas de uma empresa. São eles o gráfico de funil, o gráfico de área e o gráfico de barras.
 
## Visualização Funil
 
O gráfico de funil é bem interessante para acompanhar um ciclo de vida dos clientes, a quantidade de clientes em cada etapa e a conversão deles entre uma etapa e outra. Dessa forma é possível ter uma média de quantos leads preciso atrair para gerar uma venda.
 
Para conseguir ter uma visão desse tipo, é preciso ter os dados estruturados de forma similar a **Figura 1**. Observe que para cada lead que entra na empresa, tenho exatamente em qual etapa ele se encontra atualmente. Dessa forma conseguimos desenhar esse funil no Power BI.
 
| ![Funil](https://s3-sa-east-1.amazonaws.com/lcpi/59b2c8f1-66d5-4109-aee0-5a7e52e51497.png) |
|:--:|
| **Figura 1** – _Dados para o Funil_ (Fonte da imagem: do autor) |
 
Será preciso selecionar 2 colunas, uma que define a contagem em cada etapa, e outra que define em qual etapa será classificado. Após selecionar o visual, é preciso selecionar os dois campos que informamos anteriormente. Observe os itens em destaque na **Figura 2**. Em **vermelho** está a seleção do visual e os campos em que foram selecionados para exibir o funil, tudo isso no menu de visualizações. Já a seleção em **verde** no menu de campos, é onde temos todos os campos disponíveis e os que foram selecionados para o visual ficam marcados no checkbox. E finalizamos com a seleção **rosa**, onde o funil já é exibido na área do dashboard.
 
| ![Funil](https://s3-sa-east-1.amazonaws.com/lcpi/53ff2e48-a541-4200-85af-d67a4a881614.png) |
|:--:|
| **Figura 2** – _Gráfico de Funil_ (Fonte da imagem: do autor) |
 
### Quando utilizar a visualização de funil
*   Para acompanhar medidas de conversão
*   Entender qual o ciclo de vida dos clientes e acompanhar as etapas
 
## Visualização gráfico de área
 
Para o visual de área também será preciso selecionar 2 colunas, uma que define uma agregação, e outra que define o período. Após selecionar o visual, é preciso selecionar os campos, confere os detalhes na **Figura 3**. Em **vermelho** está a seleção do visual e os campos em que foram selecionados para exibir o gráfico de área. Já a seleção em **verde** no menu de campos, é onde temos todos os campos em que foram selecionados para o visual marcados no checkbox. E finalizamos com a seleção **rosa**, onde o gráfico de área já é exibido na área do dashboard.
 
| ![Area](https://s3-sa-east-1.amazonaws.com/lcpi/8d66081f-f9f5-4174-9cad-63d84171e07f.png) |
|:--:|
| **Figura 3** – _Gráfico de Área_ (Fonte da imagem: do autor) |
 
Os campos com o tipo de dados no formato de dados, possuem uma hierarquia definida pela própria informação **Ano > Trimestre > Mês > Dia**. Com isso é possível navegar no gráfico de forma interativa a fim de analisar os dados pelos diversos ângulos da hierarquia da data. Confere essa interação na **Figura 4** onde é feito essa navegação entre as hierarquias.
 
| ![Area](https://s3-sa-east-1.amazonaws.com/lcpi/40df70c7-81f3-4d66-9733-e2031c6b1877.gif) |
|:--:|
| **Figura 4** – _Visualizando o Gráfico de Área_ (Fonte da imagem: do autor) |
 
### Quando utilizar a visualização de área
*   Encontrar tendências nos dados ao longo do tempo
*   As áreas preenchidas mostram a amplitude dos dados
 
## Visualização gráfico de barras
 
Para o gráfico de barra é preciso definir uma coluna para o eixo x e outra para o eixo y. Após selecionar o visual, é preciso selecionar os campos conforme **Figura 5**. Em **vermelho** está a seleção do visual e os campos em que foram selecionados para exibir o gráfico de barra. Já a seleção em **verde** no menu de campos, é onde temos todos os campos em que foram selecionados para o visual marcados no checkbox. E finalizamos com a seleção **rosa**, onde o gráfico de barra já é exibido na área do dashboard.
 
| ![Barra](https://s3-sa-east-1.amazonaws.com/lcpi/3d6bff8f-d010-4832-bd66-98415955b549.png) |
|:--:|
| **Figura 5** – _Gráfico de Barra_ (Fonte da imagem: do autor) |
 
Para dar destaque para as informações mais relevantes é possível definir um filtro para visualizar apenas os valores maiores. Na **Figura 6** foi colocado um filtro de TOP5, o filtro é apenas no visual utilizando a opção **N superior** conforme seleção **vermelha**. É possível escolher a quantidade do TOP apresentado e qual o campo de valor será considerado, identificado pela seta **verde**. Com tudo configurado, o gráfico já é atualizado conforme a seleção **rosa** na área de dashboard.
 
| ![Barra](https://s3-sa-east-1.amazonaws.com/lcpi/d61406fc-b1af-4f65-b523-a3a3f3c09ba2.png) |
|:--:|
| **Figura 6** – _Filtrando TOP5_ (Fonte da imagem: do autor) |
 
### Quando utilizar a visualização de barras
*   Comparar categoria
*   Entender a distribuição dos dados
 
Novos gráficos para os dashboards! É preciso saber utilizar o melhor gráfico para cada uma das visualizações. Dessa forma, quem utiliza os dados para a tomada de decisão, pode fazer as melhores análises.
 
No próximo tópico será mostrado como transformar os dados que iremos colocar nas nossas visualizações.
 
## Referências
 
*  https://docs.microsoft.com/pt-br/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a