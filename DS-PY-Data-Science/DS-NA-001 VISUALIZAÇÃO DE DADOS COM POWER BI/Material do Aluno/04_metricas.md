# Métricas no Power BI
 
Para construir as visualizações conforme as necessidades do negócio, é preciso construir as métricas relacionadas ao negócio. Dessa forma é possível atender a todos os segmentos de negócios com o Power BI, pois é possível construir as medidas de forma customizada, ou seja, é possível criar medidas no próprio Power BI. Aqui veremos alguns conceitos importantes e uma introdução de como criar medidas personalizadas com a linguagem DAX (Data Analysis Expressions) em tradução livre Expressões de Análise de Dados.
 
## DAX
 
O DAX é uma linguagem para realizar cálculos avançados em modelos de dados tabulares, ela é utilizada no Power BI e em algumas outras ferramentas da Microsoft. Confere abaixo algumas categorias das funções DAX que são bastante comuns nos dashboards do Power BI.
 
### Funções de agregação
 
*  **AVERAGE -** Média dos números da coluna
*  **COUNT -** Contagem do número de linhas
*  **MAX -** Maior valor numérico
*  **MIN -** Menor valor numérico
*  **SUM -** Soma os valores de uma coluna
 
### Funções de data e hora
 
*  **DATE -** Retorna a data no formato datetime
*  **DATEDIFF -** Retorna o intervalo entre duas datas
*  **DAY -** Retorna o dia de uma data
*  **MONTH -** Retorna o mês de uma data
*  **YEAR -** Retorna o ano de uma data
*  **TODAY -** Retorna a data atual
 
### Funções de filtro
 
*  **AND -** Retorna TRUE se ambos os argumentos forem verdadeiros
*  **OR -** Retorna TRUE se um dos argumentos for verdadeiro
*  **IF -** Verifica se uma condição é verdadeira e retorna um valor, caso contrário, retorna outro valor
*  **NOT -** Altera uma expressão verdadeira para falsa e vice-versa.
 
### Funções de filtro
 
*  **ALL -** Retorna os valores desconsiderando os filtros aplicados
*  **FILTER -** Filtra o subconjunto de uma tabela ou expressão
 
As funções DAX que vimos acima e as demais podem ser utilizadas para criar medidas e colunas. É o que veremos a seguir.
 
## Medidas
 
As medidas são cálculos dinâmicos que interagem com o dashboard. Elas podem ser usadas para criar, por exemplo, o valor total de vendas, o total de quantidades vendidas, o ticket médio das vendas, entre muitas outras.
 
A **Figura 1** mostra como criar uma medida.
 
| ![Medida](https://s3-sa-east-1.amazonaws.com/lcpi/9ab00b7a-107b-453e-9984-460ea64e49c3.png) |
|:--:|
| **Figura 1** – _Nova Medida_ (Fonte da imagem: do autor) |
 
Após clicar no botão **Nova medida**, aparecerá uma barra de fórmula, destacada em vermelho, onde será criada a medida. Quando criada, a nova medida já estará fazendo parte do menu campo, observe o destaque em verde. Estes detalhes estão na **Figura 2**
 
| ![Medida](https://s3-sa-east-1.amazonaws.com/lcpi/d57b47dd-da93-4e58-8e58-a3b12c67fb97.png) |
|:--:|
| **Figura 2** – _Ferramentas de Medida_ (Fonte da imagem: do autor) |
 
Agora já pode inserir a função DAX, na **Figura 3** um exemplo com a agregação **SUM** no destaque vermelho. No menu campos em destaque verde, a nova medida já está pronta para o uso com o nome definido na função.
 
| ![Medida](https://s3-sa-east-1.amazonaws.com/lcpi/b49bf4da-2bae-401a-8ebe-170de35848e7.png) |
|:--:|
| **Figura 3** – _DAX_ (Fonte da imagem: do autor) |
 
E finalmente podemos criar uma visualização com a medida que foi criada. A **Figura 4** mostra todos os detalhes. Em **vermelho** a visualização escolhida do tipo rosca e os campos utilizados, para o valor do gráfico selecionada a nova medida e um outro campo para a legenda. Em **verde**, todos os campos utilizados na visualização com o checkbox marcado. E por fim, em **rosa**, a visualização pronta na área do dashboard.
 
| ![Medida](https://s3-sa-east-1.amazonaws.com/lcpi/5b1fc150-c76e-4c75-8232-ed633a5206e6.png) |
|:--:|
| **Figura 4** – _Visualização com Medida_ (Fonte da imagem: do autor) |
 
Agora aprenderemos a criar colunas para os dados.
 
## Colunas
 
Uma nova coluna pode ser criada a partir de um cálculo utilizando as fórmulas DAX, assim a tabela passa ter uma nova coluna para ser utilizada nos dashboards. Um exemplo seria a criação de 3 novas colunas a partir de uma coluna de data, onde teria uma nova coluna para o dia da data, outra para o mês e uma terceira com o ano.
 
A **Figura 5** mostra como criar uma coluna através do menu modelagem.
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/b871f80a-92c2-48c4-b97b-a8d7006ebef5.png) |
|:--:|
| **Figura 5** – _Nova coluna_ (Fonte da imagem: do autor) |
 
Após clicar no botão **Nova coluna**, aparecerá uma barra de fórmula, destacada em vermelho, onde será criada a coluna. Quando criada, a nova coluna já estará fazendo parte do menu campo, observe o destaque em verde. Estes detalhes estão na **Figura 6**
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/43824fe3-2ad1-4a36-92a6-450efc19d57d.png) |
|:--:|
| **Figura 6** – _Ferramentas de Coluna_ (Fonte da imagem: do autor) |
 
Agora já pode inserir a função DAX, na **Figura 7** um exemplo com a função de data **YEAR** no destaque vermelho. No menu campos em destaque verde, a nova coluna já está pronta para o uso com o nome definido na função.
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/bbe7376a-9b04-47ba-abea-dd4d32911b7f.png) |
|:--:|
| **Figura 7** – _DAX_ (Fonte da imagem: do autor) |
 
É possível consultar os dados da nova coluna ao nível de tabela, na lateral esquerda podemos navegar até as tabelas carregadas, conforme a **Figura 8**, assim é possível fazer um check da coluna criada.
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/b703aef1-4611-4c4f-a5de-135381fa1d06.png) |
|:--:|
| **Figura 8** – _Dados Nova Coluna_ (Fonte da imagem: do autor) |
 
Chegou a hora de criar uma visualização com a coluna que foi criada. A **Figura 9** mostra todos os detalhes. Em **vermelho** a visualização escolhida do tipo segmentação de dados e o campo utilizados, que foi a coluna criada. Em **verde**, todos os campos utilizados na visualização com o checkbox marcado. E por fim, em **rosa**, a visualização pronta na área do dashboard.
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/ad7a5b99-3bd6-4a8b-8631-4a34dc0df2a9.png) |
|:--:|
| **Figura 9** – _Visualização com Nova Coluna_ (Fonte da imagem: do autor) |
 
Para finalizar observe a **Figura 10**, uma demonstração dos dados da nova coluna sendo utilizado como filtro do dashboard.
 
| ![Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/ab4eb51c-2fe4-4634-809f-7d58e6a260d5.gif) |
|:--:|
| **Figura 10** – _Filtro com Nova Coluna_ (Fonte da imagem: do autor) |
 
Resolvido! Com a criação de novas medidas e novas colunas, o desenvolvedor tem a liberdade de criar as métricas conforme a necessidade do negócio.
 
No próximo tópico será mostrado como criar mais algumas visões no Power BI.
 
## Referências
 
*  https://docs.microsoft.com/pt-br/dax/
