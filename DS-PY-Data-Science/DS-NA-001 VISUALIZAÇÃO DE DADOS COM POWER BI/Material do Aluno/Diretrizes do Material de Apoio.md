# Diretrizes para produção de material de apoio

## Introdução

O plano pedagógico da Let’s Code foi desenvolvido com base em algumas metodologias de ensino que se alinham com a nossa visão de educação. O aluno está no centro do processo de aprendizagem e não queremos em nenhum momento pensar por ele.

Para isso, escolhemos entre as metodologias de ensino aquelas que tem o potencial para o desenvolvimento da autonomia do aluno e para o crescimento dele durante o curso.

As duas principais metodologias de ensino escolhidas, que se relacionam com a produção de material, são:

Sala de aula invertida, que implica que o aluno deve colocar uma certa quantidade de esforço em casa para um aprendizado autodidata apoiado pelo material. Assim, incentivamos o desenvolvimento de sua autonomia.

Aprendizado baseado em problemas/projetos, que implica uma saudável quantidade de problemas de escopo aberto para incentivar o desenvolvimento de um pensamento mais abrangente, não limitado a pequenos objetivos ou a um único caminho de resolução.

Todos os cursos da Let’s Code devem ter um material de apoio, dividido de acordo com os módulos do curso (quando aplicável), que seja capaz de apoiar o aluno em seus estudos autônomos, de forma que possa ser seguido sem a presença do professor.

Para isso ele deverá ter uma organização lógica, incremental e ordenada.

Para garantir maior aderência aos objetivos de nossas metodologias colocamos as seguintes diretrizes para a produção de material complementar.

## Diretrizes da produção de material de apoio

Abaixo estão as diretrizes de produção de material de apoio divididas entre normativas, relacionadas a forma e conteúdo, e qualitativas relacionadas ao texto do material.

### Diretrizes normativas

1. Todos conceitos descritos na ementa de um módulo devem estar presentes no material de apoio.

2. Para cada conceito deve haver uma descrição, a contextualização (para que serve, como é usado, como se relaciona com outros conceitos) e exemplos em código (se aplicável).

3. O conteúdo deve ser apresentado em formato markdown.

4. Exemplos de código devem estar devidamente formatados em bloco de código, com a linguagem especificada. Palavras que referem ao código como nomes de função deve estar em formato de código inline.

5. Não use o aportuguesamento de empréstimos linguísticos como codar, buildar, deployar, upar, etc… Na escrita do material devemos ter um certo rigor então esses termos não funcionam. Fazer um build, fazer um deploy, podem ser usados, se não houver bom substituto em português.

6. Cite as referências utilizadas e a fonte de imagens e tabelas.  

7. Para nomear o arquivo markdown utilize uma numeração seguida do nome do conceito (Ex.: 01_Variaveis, 02_Estruturas_Condicionais). Enumere os arquivos de acordo com a ordem que o conceito é apresentado dentro do módulo.

8. O material de apoio deve ser entregue pelo gitlab, por meio de merge request. Será feita uma avaliação do tipo *peer review* do material antes de ser aceito no repositório. Os caminhos para os repositórios serão enviados antes do início da produção do material.


### Diretrizes qualitativas

**1. Material de apoio não é o mesmo que material de aula**

O material de apoio é um material genérico abordando os conceitos principais trabalhados no módulo. Ele não deve ser dividido aula a aula e não tem o intuito de ser utilizado em sala de aula pelo professor. 

Materiais para uso em aula como apresentações, exemplos e etc…   são de responsabilidade do professor que estiver ministrando o módulo. 

**2. O material de apoio deve ter profundidade teórica**

Preferimos que nossas aulas sejam dinâmicas e hands-on, quanto mais o aluno se mantiver praticando, melhor. Sendo assim, não temos oportunidade de aprofundar a parte teórica. O material de apoio deve ser pensado de forma a suprir essa demanda, oferecendo um aprofundamento teórico maior que o de sala de aula e não apenas um overview de um parágrafo de cada termo ou conceito.

**3. O material de apoio pode ser pensado como um ebook**

O material de apoio pode ser pensado como um livro, com uma teoria mais aprofundada sobre os assuntos do módulo e com uma linha lógica entre os conteúdos. 

Não há problemas em estender a teoria, no entanto, os autores devem escolher com cuidado os temas que desejam abordar. 

Como balizador, escolha conhecimentos, que (a) são essenciais ao aluno para o bom aproveitamento do curso, (b) são essenciais a todos os profissionais que trabalham dentro da área de formação do curso, (c) são essenciais a todos profissionais de tecnologia, (d) são diferenciais na escolha de um candidato para trabalhar na área de formação do curso.

O que estiver fora das categorias citadas, que tiver pouca aplicabilidade prática ou, que for marginal ao assunto do módulo, pode ser abordado de forma rasa ou não abordado.

Tópicos fora dessa baliza que o autor julgar interessantes de abordar em profundidade devem ser marcados como opcionais (com [opcional]) antes do título, e uma ou duas linhas descrevendo que é um conteúdo opcional, e os motivos pelo qual ele entende que o conteúdo é interessante o suficiente para estar no material, ficando assim de aprofundamento para alunos mais empenhados.

**4. O material pode ser uma narrativa**

Não é problema falar com o aluno, fazer perguntas retóricas, instigar observações, pesquisas e etc… no material de apoio. Uma voz narrativa capaz de deixar o estudo mais leve é incentivada, uma ou outra brincadeira, não é problema. Um tom um pouco mais coloquial e jovem também é desejável. 

No entanto, deve-se restringir esse estilo de escrita às explicações mais abrangentes, contextualizações, aos cenários de aplicação, e storytelling. 

Procure fazer uma narrativa incremental, onde os conceitos vão se somando e chegam a algum propósito no final, que dependa deles, evitando deixá-los soltos. Esse propósito pode ser um programa, ou algoritmo, um projeto, etc… 

**5. O material deve ter rigor acadêmico**

Apesar da voz narrativa leve colocada no tópico anterior, na hora da explicação de conceitos, técnicas, e descrição de passos práticos deve-se retomar uma voz rigorosa, com vocabulário preciso, sem coloquialismos ou neologismos de forma que fique absolutamente claro o conceito em explicação. Não há espaço para brincadeiras ou exemplos mais levianos na explicação de conceitos importantes ou na descrição de passos práticos. 

Lembre-se que a criação de vocabulário é parte essencial do curso, não queremos que o aluno apenas saiba, mas que também se expresse como alguém que sabe, portanto, se um conceito tem um nome, devemos sempre chamá-lo pelo nome, sem apelidos.

Para facilitar a assimilação de um conceito sempre opte por usar uma abundância de exemplos em vez de rebaixar a linguagem.

**6. Não precisamos transformar tudo em teoremas matemáticos**

Essa é uma diretriz com dois lados, um diz respeito a diretriz anterior, não precisamos ir tão longe nela, que as explicações pareçam a descrição de teoremas matemáticos. Existe um meio termo saudável entre as descrições matemáticas intragáveis e o coloquialismo, é nesse meio termo que devemos procurar estar.

O outro lado é, apesar de sermos quase todos de exatas, nossos alunos não são todos ligados à matemática. Se é possível dar um exemplo mundano, que explicite bem um caso e um exemplo matemático, que explique bem o mesmo caso, opte pelo mundano.

Nosso aluno vai ter muito mais interesse em usar um laço para percorrer uma lista de fotos de gatinho baixada do instagram do que pra calcular o 30o termo de uma progressão geométrica.

**7. O material não deve ser uma cópia da documentação**

Uma das críticas mais recorrentes aos cursos livres é que são apenas a documentação da linguagem/tecnologia em forma de curso.

Não fazemos isso aqui. 

No material do aluno, não devemos colocar as mesmas coisas que estão na documentação, ao contrário, ele deve mandar o aluno à documentação oficial sempre que necessário (todos devem saber recorrer à documentação, é parte fundamental do desenvolvimento da autonomia).

Algumas vezes isso pode ser difícil porque documentações de qualidade, como a do React, por exemplo, são divididas nos conceitos principais da mesma forma que abordamos no curso...

Quando esse for o caso opte por fazer um projeto no material, que aborde os conceitos em paralelo com a prática. Se possível evitando as mesmas temáticas de projeto, que foram usadas na documentação e procure no mesmo projeto abordar mais de um conceito de forma incremental.

**8. Não tenha medo de complexidade**

O material de apoio é o lugar mais seguro para subirmos o nível e adicionarmos um pouco mais de complexidade. Exemplos que precisam de diversos conceitos, operando em sinergia para produzir um resultado, são os mais desejáveis.

Na complexidade da relação entre os conceitos que fazemos um curso melhor do que a documentação pode oferecer. Conceitos soltos, em aplicações simplistas, são muito fáceis de ensinar, mas não representam código real, tem pouco valor prático, queremos proporcionar ao aluno uma experiência de codificar como no dia a dia de um programador de verdade.

**9. O material deve ter um planejamento do módulo e das aulas**

Cada módulo deve ter um planejamento tanto do módulo em si quanto das aulas, você o receberá no momento em que for iniciar sua produção. Este planejamento servirá como base para sua produção, mas lembre-se sempre, você não deve produzir o material do aluno com base na aula a aula no planejamento, mas poderá utilizar os conceitos contidos no quadro de planejamento do módulo para produzi-lo.

No planejamento existem problemas geradores, utilize-os na introdução dos tópicos do material do aluno.

Cada tópico deverá ser iniciado com uma introdução.

**10. O material deve conter indicação de materiais complementares**

O material do aluno, como já dito anteriormente, deve abordar tópicos importantes para a formação dos alunos, porém, não precisa ser tão profundo quanto um livro técnico e/ou acadêmico. 

Por isso, é importante fazer indicação de materiais complementares aos alunos para que eles possam se aprofundar nos tópicos abordados nas aulas que, talvez, não estejam presentes no material do aluno.

Lembre-se que o aluno utilizará este material como fonte de pesquisa. Portanto, ofereça materiais com fonte confiáveis.

Estes materiais poderão ser vídeos, podcasts, livros, artigos, filmes e outros tipos que servirão como aprimoramento do módulo estudado. 

Lembre-se que a Let's Code possui um canal no [YouTube](https://www.youtube.com/c/LetsCodeBR) e um [Blog](https://letscode.com.br/blog). Se possível, cite vídeos e publicações dessas fontes. É uma ótima maneira de estimular a conexão entre o aluno e a escola. Além disso, fique atento para não citar materiais de concorrentes diretos da Let's Code.

**11. Modelo de desenvolvimento do material do aluno**

1. Todo material do aluno precisa de uma introdução por tópico. Escreva um texto breve sobre o que será abordado no material visando incentivar a leitura completa do aluno. Lembre-se de desenvolver uma escrita coerente, coesa e atrativa.

3. Os objetivos também precisam estar presentes, descreva quais serão os resultados concretos que o tópico a ser desenvolvido pretende alcançar. 

4. No desenvolvimento do material, você poderá utilizar de tópicos e subtópicos para descrever o conteúdo. Organize-o de maneira clara pensando na capacidade de interpretação dos alunos. Lembre-se de de interligar os parágrafos, dando continuidade a ideia do assunto abordado no tópico que está sendo desenvolvido.

4. Ao final do material, escreva uma conclusão retomando o assunto que foi abordado de maneira analítica, ou seja, sem repetir o que já foi dito no desenvolvimento, mas trazendo uma discussão que acrescente algo no conteúdo.


5. Lembre-se de citar as referências e adicionar os materiais complementares em cada tópico.


**12. Sobre o processo de entrega do material do aluno**

A entrega do material do aluno deverá ser feita de maneira parcial de acordo com o tempo proposto para a produção (15 dias). 

Você será informado sobre esse processo pelo responsável pedagógico que entrará em contato para falar sobre a produção.

**13. Tutoriais e instruções básicas que podem te ajudar**

[Tutorial para incluir imagens e arquivos no material de apoio](https://gitlab.com/letscode-pedagogico/documentos-pedagogicos/-/blob/master/Tutorial_para_adi%C3%A7%C3%A3o_de_imagens_e_arquivos.md)

[Instruções básicas para a utilização da linguagem Markdown](https://gitlab.com/letscode-pedagogico/documentos-pedagogicos/-/blob/master/Instru%C3%A7%C3%B5es_b%C3%A1sicas_Markdown.md)

**14. Exemplo de material do aluno (texto e conteúdo)**

No link abaixo você encontrará um material sobre Web API (API do navegador), que pode ser usado como exemplo de qualidade tanto na escrita quanto no conteúdo. Mas, atenção, o material não está completo, nele não contém todos os elementos necessários que são abordados nas diretrizes de produção de material, como materiais complementares, referências etc. Por isso, atente-se apenas à forma como ele foi escrito e muito bem dividido:


[Clique aqui para visualizar o material.](https://gitlab.com/letscode-pedagogico/materiais-antigos/-/blob/dbc0d4a4498bf78bb78764d89e3fd87abe11075b/Web%20Front%20End%20React/06_React/01%20Web%20API%20-%20API%20do%20navegador.md)

