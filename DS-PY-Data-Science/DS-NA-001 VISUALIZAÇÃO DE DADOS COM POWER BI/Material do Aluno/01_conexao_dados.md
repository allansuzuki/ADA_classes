# Conexão com os dados no Power BI
 
Neste módulo será apresentado como utilizar a ferramenta Power BI para a visualização de dados. Para começar faremos um tour na ferramenta, desde a instalação até a conexão com as bases de dados. Mas antes, alguns conceitos importantes.
 
## O que é o Power BI?
 
O Power BI é uma ferramenta de visualização de dados proprietária da Microsoft. Porém, ele possui uma versão desktop grátis para download. Com ela é possível construir dashboards, pois possui diversas opções de gráficos nativos. Também é possível adicionar gráficos construídos pela comunidade. Outra funcionalidade disponível é a integração com as linguagens de programação R e Python, deixando a ferramenta um pouco mais flexível. Não podemos esquecer da linguagem DAX, que é uma biblioteca de funções e operadores que deixa o desenvolvedor com muita liberdade para criar as métricas e transformar em visualizações.
 
## O que é visualização de dados?
 
Visualização de dados também é conhecido como dataviz, sendo no seu sentido mais puro a representação visual de dados. É transformar dados brutos em tabelas e gráficos para responder perguntas sobre algum negócio.
 
## O que é um dashboard?
 
É um painel de indicadores, que pode dar mais controle ao negócio ou também gerar insights. O principal objetivo do dashboard é facilitar a tomada de decisão de uma forma rápida e baseada em dados. Em que o gestor tem dados sobre o negócio de forma resumida e responde a perguntas sobre o seu negócio.
 
Um exemplo clássico é um painel do automóvel, que serve justamente para controlar os indicadores de velocidade, temperatura, combustível, dentre outras coisas, tudo isso de forma objetiva e clara, para que o condutor possa tomar decisões.
 
## Instalando o Power BI
 
Para fazer o download do Microsoft Power BI Desktop, basta acessar o [link no site da Microsoft](https://www.microsoft.com/pt-BR/download/details.aspx?id=58494) e escolher o programa 32 ou 64 bits.
 
Utilizaremos aqui a versão **2.108.603.0** do Power BI, conforme Figura 1.
 
| ![Versão Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/f59f8f9a-6f95-4668-9cc1-0f837fc3ec6e.png) |
|:--:|
| **Figura 1** – _Versão Power BI_ (Fonte da imagem: do autor) |
 
Após a instalação da ferramenta, seguimos para conhecer a sua tela inicial.
 
## Conhecendo o Power BI
 
Na Figura 2, temos em destaque as principais partes do Microsoft Power BI Desktop, que estão separadas por cor:
*   **Marrom:** Seleciona o tipo de visualização em dashboard, dados ou relacionamentos.
*   **Azul:** As páginas de desenvolvimento de dashboards.
*   **Rosa:** Área para desenvolvimento dos dashboards.
*   **Amarelo:** Opções de filtros do Power BI.
*   **Vermelho:** Opções de visualizações do Power BI, e ajustes dos gráficos selecionados.
*   **Verde:** Dados carregados, organizados em tabelas e colunas.
 
| ![Tour Power BI](https://s3-sa-east-1.amazonaws.com/lcpi/0ef80a09-d41b-4d8c-b7ea-351922a776ce.png) |
|:--:|
| **Figura 2** – _Tour Power BI_ (Fonte da imagem: do autor) |
 
Após esse tour na ferramenta com as principais partes, pode ser feita a conexão com os dados e começar. Criar visualizações.
 
## Acesso a dados via Excel
 
Primeiramente faremos a conexão com uma base de dados no Excel, acessando o caminho **Arquivo > Obter dados > Pasta de trabalho do Excel**, conforme a Figura 3.
 
| ![Obter Dados Excel](https://s3-sa-east-1.amazonaws.com/lcpi/8faccb52-c885-4c81-a907-ce0817eddf21.png) |
|:--:|
| **Figura 3** – _Obter Dados Excel_ (Fonte da imagem: do autor) |
 
Selecionado a opção do Excel, será solicitado a escolha do arquivo salvo na máquina, igual à Figura 4.
 
| ![Selecionando Arquivo Excel](https://s3-sa-east-1.amazonaws.com/lcpi/1ef5f770-a223-438a-b2a3-632707dea577.png) |
|:--:|
| **Figura 4** – _Selecionando Arquivo Excel_ (Fonte da imagem: do autor) |
 
Após selecionar o arquivo, já é possível ver uma prévia dos dados. A Figura 5 mostra exatamente uma prévia dos dados selecionados.
 
| ![Prévia dos Dados Excel](https://s3-sa-east-1.amazonaws.com/lcpi/e0744dd3-611c-46c5-a053-892585368f0c.png) |
|:--:|
| **Figura 5** – _Prévia dos Dados Excel_ (Fonte da imagem: do autor) |
 
Após clicar no botão Carregar, é só aguardar alguns segundos e já teremos os dados para trabalhar. Na Figura 6, é possível ver onde estão localizados os atributos da tabela carregada na tela de criação dos dashboards.
 
| ![Dados no Dashboard](https://s3-sa-east-1.amazonaws.com/lcpi/b4782473-ef8e-4289-ad6e-3154d730d5f5.png) |
|:--:|
| **Figura 6** – _Dados no Dashboard_ (Fonte da imagem: do autor) |
 
Seguindo o menu lateral à esquerda, onde está sinalizado com uma seta, é possível visualizar os dados carregados. Observe a Figura 7.
 
| ![Dados Carregados](https://s3-sa-east-1.amazonaws.com/lcpi/ac13960c-3340-4878-9b18-b4ef62214487.png) |
|:--:|
| **Figura 7** – _Dados Carregados_ (Fonte da imagem: do autor) |
 
Na Figura 8 são apresentados os relacionamentos dos dados, no exemplo apresentado, só temos uma tabela carregada, é possível também, definir algumas propriedades dos dados.
 
| ![Relacionamentos dos Dados](https://s3-sa-east-1.amazonaws.com/lcpi/4fdc23a0-52ed-46bf-a628-6600020c56e4.png) |
|:--:|
| **Figura 8** – _Relacionamentos dos Dados_ (Fonte da imagem: do autor) |
 
Agora é só partir para a criação das visualizações, mas antes, veremos como conectar a uma base de dados SQL.
 
## Acesso a dados via SQL
 
Para a conexão com uma base de dados SQL, acessar o caminho **Arquivo > Obter dados > Obter dados para começar**, conforme a Figura 9.
 
| ![Obter Dados SQL](https://s3-sa-east-1.amazonaws.com/lcpi/5cb6386e-d31d-4f8b-9d1b-0e37e5500bfc.png) |
|:--:|
| **Figura 9** – _Obter Dados SQL_ (Fonte da imagem: do autor) |
 
Como na Figura 10, selecionar a opção **Banco de Dados**, em seguida escolher o tipo do banco. Para os exemplos a seguir será apresentado a configuração com o banco de dados PostgreSQL.
 
| ![Obter Dados PostgreSQL](https://s3-sa-east-1.amazonaws.com/lcpi/759f44b2-2a12-4881-adca-034e288fc2f1.png) |
|:--:|
| **Figura 10** – _Obter Dados PostgreSQL_ (Fonte da imagem: do autor) |
 
Na Figura 11, um exemplo de configuração para conectar a uma base do PostgreSQL, informar o **servidor** (localhost, uma base local na máquina onde está instalado o Power BI) e o **Banco de Dados** (ibge, nome da base de dados utilizada no exemplo)
 
| ![Configuração PostgreSQL](https://s3-sa-east-1.amazonaws.com/lcpi/09b65352-c898-4fe0-8f5e-07b8ff7ca163.png) |
|:--:|
| **Figura 11** – _Configuração PostgreSQL_ (Fonte da imagem: do autor) |
 
Então seguimos para as configurações de segurança na Figura 12, informar o **Nome de usuário** e **senha** da base de dados para a conexão.
 
| ![Configuração Segurança PostgreSQL](https://s3-sa-east-1.amazonaws.com/lcpi/7555e42f-69d9-449b-83f7-a1ea86436224.png) |
|:--:|
| **Figura 12** – _Configuração Segurança PostgreSQL_ (Fonte da imagem: do autor) |
 
Após selecionar as configurações do banco de dados, já é possível ver uma prévia dos dados. A Figura 13 mostra exatamente uma prévia dos dados selecionados.
 
| ![Prévia Dados PostgreSQL](https://s3-sa-east-1.amazonaws.com/lcpi/720d3661-2d44-446e-b108-77b256ba30b8.png) |
|:--:|
| **Figura 13** – _Prévia Dados PostgreSQL_ (Fonte da imagem: do autor) |
 
Após clicar no botão Carregar, é só aguardar alguns segundos e já teremos os dados do banco PostgreSQL para trabalhar. Na Figura 14, é possível ver onde estão localizados os atributos da tabela carregada na tela de criação dos dashboards.
 
| ![Dados no Dashboard](https://s3-sa-east-1.amazonaws.com/lcpi/fd854ff5-1f66-4207-810f-c84f776878ed.png) |
|:--:|
| **Figura 14** – _Dados no Dashboard_ (Fonte da imagem: do autor) |
 
Seguindo o menu lateral à esquerda, como fizemos anteriormente, onde está sinalizado com uma seta, é possível visualizar os dados carregados. Observe a Figura 15.
 
| ![Dados Carregados](https://s3-sa-east-1.amazonaws.com/lcpi/688059e5-4b1a-4b92-8fa9-8422d5ce27f7.png) |
|:--:|
| **Figura 15** – _Dados Carregados_ (Fonte da imagem: do autor) |
 
Finalizamos com a Figura 16 onde temos os relacionamentos dos dados, no exemplo apresentado, só temos uma tabela carregada, é possível também, definir algumas propriedades dos dados.
 
| ![Relacionamentos dos Dados](https://s3-sa-east-1.amazonaws.com/lcpi/713ff82f-8de8-4ac1-a5a6-d505254452bd.png) |
|:--:|
| **Figura 16** – _Relacionamentos dos Dados_ (Fonte da imagem: do autor) |
 
Pronto! Já temos a configuração das conexões de Excel e do PostgreSQL, as demais conexões são similares salvo as particularidades de cada uma.
 
No próximo tópico já daremos os primeiros passos para construções das visualizações.
 
## Referências
 
*  https://powerbi.microsoft.com/pt-br/what-is-power-bi/
*  https://powerbi.microsoft.com/pt-br/downloads/
*  https://docs.microsoft.com/pt-br/power-bi/
