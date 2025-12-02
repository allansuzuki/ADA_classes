# Dashboard no Power BI  
 
Agora já vimos os principais detalhes para criar um dashboard. Começamos conhecendo algumas visualizações, depois aprendemos como fazer os filtros, em seguida as funções DAX e finalizamos com mais algumas visualizações.
 
Chegou a horas de juntar todos esses elementos para criar um dashboard. Um detalhe bastante importante é a granularidade dos dados, conheceremos a teoria por trás desse tema e partimos para estruturar o dashboard.
 
## Granularidade
 
A granularidade dos dados vai definir o quão detalhados são os dados. Quanto maior a granularidade maior o nível de detalhe apresentado, quanto menor a granularidade menor o nível de detalhes, são os dados sumarizados ou agregados. Conforme a granularidade dos dados podemos realizar algumas operações com eles. Observe a **Figura 1** que mostra as formas possíveis de visualizar os dados.
 
| ![Dados](https://s3-sa-east-1.amazonaws.com/lcpi/2d65678d-237b-4a8f-8ecf-1b32b9603b58.png) |
|:--:|
| **Figura 1** – _Operações com dados_ (Fonte da imagem: internet, autor desconhecido) |
 
*   **Slicing –** Fatiar os dados e selecionar uma dimensão.
*   **Dicing –** Cortar dados e selecionar duas ou mais dimensões.
*   **Pivot –** Rotacionar os dados e mudar a perspectiva de visualização.
*   **Drill Down –** Maior granularidade, detalhar os dados e aumentar o nível de detalhe dos dados.
*   **Roll UP –** Menor granularidade, generalizar os dados e diminuir o nível de detalhe dos dados.
 
Conhecendo os dados e sabendo a que nível de detalhes é possível chegar, agora é construir o dashboard.
 
## Montagem do dashboard
 
Para montar o dashboard e deixar ele mais atraente, precisaremos de mais algumas coisas além dos gráficos. Então criaremos um menu superior para organizar, logo, título e filtros do dashboard.
 
### Formas
 
Podemos organizar algumas informações no dashboard com o recurso de formas. Na **Figura 2** os detalhes de como inserir formas através do menu inserir e botão de formas.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/81156f17-680c-474f-90ab-b42017dc93b0.png) |
|:--:|
| **Figura 2** – _Incluindo Formas_ (Fonte da imagem: do autor) |
 
Após inserir a forma desejada, ajustamos o tamanho e a posição conforme destaque em **rosa** na área de dashboard. Algumas outras configurações podem ser ajustadas no menu de formato, destacado em **vermelho** na **Figura 3**.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/a2ecd4e5-4a46-4db5-80e8-ee47743d3811.png) |
|:--:|
| **Figura 3** – _Editando Formas_ (Fonte da imagem: do autor) |
 
Agora colocaremos uma logo no menu superior.
 
### Imagens
 
Para inserir imagens no dashboard, seguimos no menu inserir no botão imagem e selecionamos a imagem desejada. A imagem é exibida na área do dash conforme destaque em **rosa** na **Figura 4**.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/9d1cc321-8f75-4759-be48-5c2b706d9cc4.png) |
|:--:|
| **Figura 4** – _Incluindo Imagens_ (Fonte da imagem: do autor) |
 
Chegou a hora de colocar o título do dashboard.
 
### Textos
 
Para organizar o dashboard é possível inserir textos no dashboard, também no menu inserir a partir do botão Caixa de texto, em destaque **vermelho** na **Figura 5**. Já o destaque **rosa**, mostra a caixa de texto na área do dashboard.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/18b6d817-bb43-4d78-a071-57295a7a27c4.png) |
|:--:|
| **Figura 5** – _Incluindo Texto_ (Fonte da imagem: do autor) |
 
A **Figura 6** mostra alguns detalhes de formatação da caixa de texto, como a formatação do texto e retirada da tela de fundo do texto.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/27b01115-d3a9-4555-9ac5-774b2c0d0e60.png) |
|:--:|
| **Figura 6** – _Editando Texto_ (Fonte da imagem: do autor) |
 
Completaremos o menu com alguns filtros.
 
### Filtros
 
Podemos inserir filtros no dashboard exemplificado na **Figura 7**. No menu visualizações, destacado em **vermelho**, selecionar o visual de segmentação de dados e escolher o campo para filtro. No menu campos, selecionado em **verde** o campo utilizado no filtro. E na área do dashboard em **rosa** o filtro.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/3027923e-827e-43c8-a36d-92eceebdc6d7.png) |
|:--:|
| **Figura 7** – _Incluindo Filtro_ (Fonte da imagem: do autor) |
 
A **Figura 8** mostra como alterar o tipo de segmentação para menu suspenso.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/10a029ed-2566-43aa-9a63-cf36aa5c1901.png) |
|:--:|
| **Figura 8** – _Editando Filtro_ (Fonte da imagem: do autor) |
 
Observe como fica o tipo de filtro selecionado, com os dados embutidos, e somente exibidos conforme seleção do usuário. Exemplo na **Figura 9**.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/9bf8b1b5-4e26-4386-9423-ff7a033030c4.png) |
|:--:|
| **Figura 9** – _Filtro Suspenso_ (Fonte da imagem: do autor) |
 
Após finalizado o visual do filtro podemos duplicar, utilizando a opção de copiar visual mostrado na **Figura 10**. Assim aproveitamos todas as formatações aplicadas, alterando somente o campo utilizado como filtro.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/5ff1f0ab-8071-4a19-a1ce-e4a6d8e1076d.png) |
|:--:|
| **Figura 10** – _Copiar Visual_ (Fonte da imagem: do autor) |
 
Após a inclusão dos dois filtros, confere o menu do dashboard de Vendas.
 
### Menu
 
Na **Figura 11** o menu completo. Temos a logo, um título, dois filtros e a forma delimitando a área do menu do dashboard.
 
| ![Menu](https://s3-sa-east-1.amazonaws.com/lcpi/487ca7ad-1b5a-4752-bea5-12b3fa43c036.png) |
|:--:|
| **Figura 11** – _Menu Dashboard_ (Fonte da imagem: do autor) |
 
Agora selecionaremos os gráficos que aprendemos nas aulas anteriores.
 
### Gráficos
 
O primeiro gráfico será o funil, mostrado na **Figura 12**. Ele apresenta as informações do ciclo de vida dos leads até a venda, com informações importantes como as quantidades por etapa e a conversão de leads em vendas.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/26b01099-eed9-4ba5-8c73-1f8f417633e8.png) |
|:--:|
| **Figura 12** – _Gráfico de Funil_ (Fonte da imagem: do autor) |
 
O segundo gráfico será o de área, exibido na **Figura 13**. Com ele teremos a evolução do valor de venda ao longo do tempo.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/90ee38f6-16f5-4b99-b1d0-fb664ffa7605.png) |
|:--:|
| **Figura 13** – _Gráfico de Área_ (Fonte da imagem: do autor) |
 
E para finalizar, na **Figura 14** o gráfico de barras. Apresentando a quantidade de leads por estados, dá para ver claramente os estados com mais e menos leads.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/968e6ff5-fd6c-47a4-a89e-71ff0f705dd5.png) |
|:--:|
| **Figura 14** – _Gráfico de Barras_ (Fonte da imagem: do autor) |
 
Após selecionar todos os gráficos, podemos incluir os mesmos junto com o menu criado no dashboard de vendas. A **Figura 15** mostra o dashboard completo, com o menu e os gráficos incluídos.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/01876193-8659-4d4f-865e-7aa7ff36c9e2.png) |
|:--:|
| **Figura 15** – _Gráficos_ (Fonte da imagem: do autor) |
 
Com todas essas informações podemos estar respondendo todas as perguntas do negócio e levando informações para a tomada de decisão. Mas é possível deixar o dashboard mais atraente e menos poluído, além de acompanhar a identidade visual.
 
### Dashboard
 
Para o dashboard final apresentado na **Figura 16** foram feitos alguns ajustes de formatação. As cores dos gráficos para acompanhar a identidade visual. Também foram alterados os títulos para deixar mais claro a quais perguntas do negócio cada gráfico responde. Retirados alguns valores dos eixos y, quando possível e incluindo rótulos nos gráficos. E para finalizar delimitadores visuais em cada gráfico.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/f8b50d46-7bbf-4c00-93d7-8e31482a1d7e.png) |
|:--:|
| **Figura 16** – _Dashboard_ (Fonte da imagem: do autor) |
 
Fechamos com o dashboard em atividade na **Figura 17**. Utilização dos filtros incluídos no menu superior e utilização dos efeitos de Drill Down e Roll UP no gráfico de área, alterando a análise de vendas ao longo do tempo.
 
| ![dash](https://s3-sa-east-1.amazonaws.com/lcpi/35e1c824-80ff-4ec5-951e-8a63d7fd9b6d.gif) |
|:--:|
| **Figura 17** – _Dashboard de Vendas_ (Fonte da imagem: do autor) |
 
E então, o primeiro dashboard! Agora é praticar, colocar as técnicas nos dashboards e o mais importante, criar dashboards para resolver problemas de negócio!
 
No próximo tópico será mostrado como publicar os dashboards criados no Power BI.
 
## Referências
 
*  Livro - Storytelling Com Dados: Um Guia Sobre Visualização De Dados Para Profissionais De Negócios (Cole Nussbaumer Knaflic)