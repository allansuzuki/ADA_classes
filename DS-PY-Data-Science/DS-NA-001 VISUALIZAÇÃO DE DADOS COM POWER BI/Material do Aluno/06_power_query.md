# Power Query
 
Uma das principais ferramentas para normalizar dados no Power BI é o Power Query. Dentro dele, é possível fazer diversas transformações como alterar nomes de colunas, preencher dados nulos, alterar tipos, criar colunas condicionais, enfim, preparar os dados que iremos utilizar em nossos datasets. Vamos explorar algumas dessas funcionalidades nas seções deste tópico.

Como exemplo, utilizaremos o dataset [audible](https://www.kaggle.com/datasets/snehangsude/audible-dataset), neste dataset temos um conjunto de dados sobre audiobooks. No *audible_uncleaned.csv* encontramos a versão não tratada desses dados, que serão um bom ponto de partida para nossos estudos!
 
## Mudança de tipo de dados
 
Quando importamos dados para o Power BI utilizando uma fonte de dados que não carregue a informação de tipo (um csv por exemplo), há a possibilidade de que o Power BI faça a inferência do tipo incorreto de dado. 

A **Figura 1** mostra a coluna release date que teve seu tipo inferido incorretamente como texto.

| ![Dado tipado incorretamente](https://s3-sa-east-1.amazonaws.com/lcpi/b363e3e7-c05b-4a9a-943c-171a88588011.png) |
|:--:|
| **Figura 1** – _Dado tipado incorretamente_ (Fonte da imagem: do autor) |

Para transformar o tipo de uma coluna podemos clickar com o botão direito no nome dessa coluna no Power Query, e então selecionar a opção "Alterar tipo", definindo o tipo adequado, como exibido na **Figura 2**

| ![Correção do tipo de dado](https://s3-sa-east-1.amazonaws.com/lcpi/d7598e05-4f7a-47fc-a6a3-5af88a0612c6.png) |
|:--:|
| **Figura 2** – _Correção do tipo de dado_ (Fonte da imagem: do autor) |

Fazendo isso, o Power Query adiciona a sequência de transformações a nova transformação desejada e já mostra como ficarão os dados após o comando "fechar e aplicar". Podemos ver o resultado na **Figura 3**

| ![Tipagem de dado corrigida](https://s3-sa-east-1.amazonaws.com/lcpi/38adb86a-191f-4ebc-91ff-9d7b8d0f8d90.png) |
|:--:|
| **Figura 3** – _Tipagem de dado corrigida_ (Fonte da imagem: do autor) |
 
## Ajustando o formato dos dados

As vezes podemos ter um formato de input dos dados que não é interessante para uso em nossas visualizações. Na **Figura 4** podemos ver que tanto o autor quanto o narrador do audiobook trazem uma informação repetida e inadequada

| ![Colunas Autor e Narrador com dados ruidosos](https://s3-sa-east-1.amazonaws.com/lcpi/6c942ccf-c451-47d8-a486-b25385aba4e7.png) |
|:--:|
| **Figura 4** – _Colunas Autor e Narrador com dados ruidosos_ (Fonte da imagem: do autor) |

Para resolver isso, podemos clickar com o botão direito na coluna e clickar em "Substituir Valores", o que invocará a caixa de diálogo da **Figura 5**, onde podemos preencher os trechos que desejamos substituir e as substituições que gostariam (para remover, basta deixar em branco).

| ![Dialogo de substituição de valores](https://s3-sa-east-1.amazonaws.com/lcpi/0f4fafe0-5935-4b5c-9d92-e8a28f8ebb35.png) |
|:--:|
| **Figura 5** – _Dialogo de substituição de valores_ (Fonte da imagem: do autor) |

Assim, é possível fazer a limpeza e verificar, na **Figura 6** que os dados estão mais adequados ao uso nas nossas visualizações

| ![Coluna Autor limpa](https://s3-sa-east-1.amazonaws.com/lcpi/c6723066-d471-4560-9dce-ba035ce2f103.png) |
|:--:|
| **Figura 6** – _Coluna Autor limpa_ (Fonte da imagem: do autor) |


## Separando informações agrupadas incorretamente

Na **Figura 7** podemos ver que há uma estruturação inadequada das informações na avaliação dos audiobooks, existem duas informações armazenadas: a avaliação média e também a quantidade de avaliações. Além disso, há um bloco de texto repetitivo que não se qualifica como informação para as nossas visualizações. Vamos resolver isso!

| ![Dados de avaliação bem ruidosos](https://s3-sa-east-1.amazonaws.com/lcpi/2112d276-2e96-4063-8c85-27d466fd5042.png) |
|:--:|
| **Figura 7** – _Dados de avaliação bem ruidosos_ (Fonte da imagem: do autor) |

Primeiramente, podemos apagar o texto de Ratings com o que aprendemos na seção anterior. Em seguida, podemos utilizar a função de dividir coluna, como vemos na **Figura 8**.

| ![Dividir Coluna](https://s3-sa-east-1.amazonaws.com/lcpi/a0c4bd6e-537d-4be5-aecc-3a624d03c378.png) |
|:--:|
| **Figura 8** – _Dividir Coluna_ (Fonte da imagem: do autor) |

Por fim, podemos utilizar o restante do texto como um delimitador para separar as colunas como na **Figura 9**

| ![Utilizando delimitador personalizado](https://s3-sa-east-1.amazonaws.com/lcpi/94f74b9d-b766-4476-8f8d-0d59cd80e423.png) |
|:--:|
| **Figura 9** – _Utilizando delimitador personalizado_ (Fonte da imagem: do autor) |

Por fim, podemos renomear as colunas, clickando com o botão direito e escolhendo a opção renomear, para que os nomes se adequem melhor ao que elas representam, como na **Figura 10**

| ![Nomes das colunas ajustados](https://s3-sa-east-1.amazonaws.com/lcpi/cc746c76-a006-48f2-b2a6-0db96c177b6b.png) |
|:--:|
| **Figura 10** – _Nomes das colunas ajustados_ (Fonte da imagem: do autor) |

Com o Power Query conseguimos ferramental arrumar a bagunça que era essa base de dados, e assim poderemos gerar visualizações bem legais sobre esses dados!
 
No próximo tópico será mostrado como juntar os gráficos e construir um dashboard no Power BI.

## Referências
 
*  https://learn.microsoft.com/pt-br/power-query