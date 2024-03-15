# projeto_transacoes_bancarias -- DS-PY-17 - logica de programacao II
# 
# Esse programa é um sistema de gestao de transacoes de uma conta bancária pessoal
# no qual os dados são de transações e possuem seu valor, a categoria do gasto e seu ID.
# 
# Teu objetivo é completar esse sistema CRUD (Create-Read-Update-Delete) simples 
# para ver dados de transacao da tua conta pessoal, criar, editar e excluir transações.
# Também deve fazer com que o programa NUNCA pare, ou seja,
# caso ocorra um possível erro, deve validar as entradas, detectar erros e avisar o usuário
# mas o programa não deve parar.
#
# Por favor crie uma cópia desde script .py e todos os dados na pasta `data` 
#
# Notas importantes: 
# 1. As funções que geram os dados e criam a interface do sistema já estão prontas. 
# por favor não as altere.
#
# 2. Depois das funções do sistema estão as funções do programa
# No qual podem alterar à vontade, exceto o nome das funções
# Ou seja, podem criar funções, adicionar ou remover parâmetros, 
# mas não alterar o nome das funções existentes.
#
# 3. Coloque opções de navegabilidade em cada janela que o usuário estiver.
# Por exemplo, se ele escolher a opcao "alterar transacao" sem querer, tem que ter a opcao de voltar para a tela anterior ou inicial.
#
# 4. Caso por qualquer motivo queira os dados originais novamente,
# apage a pasta `data` e inicie o programa novamente para gerar os dados.
# Os valores serão os mesmos, porém os UUID NÃO serão os mesmos!!
#
# Critérios (pontos):
#   tarefas validacoes  total
# C     10      15       25
# R     25      25       50
# U     10      10       20
# D     2.5     2.5      5
#
#
# Boa sorte e divirtam-se :)
# ------------------------------------------------------------------------------
# -----------------------
# depencies
# -----------------------
import json
import os
import uuid
import random
import sys

# -----------------------
# load settings
# -----------------------
sys.path.append('./data/')
from data import settings

# -----------------------
# SYSTEM functions 
# -----------------------
# não alterar nada das funções de system
def criar_transacoes(num_transacoes, proporcao_categorias, seed=settings.seed):
    assert sum([proporcao_categorias[k] for k in proporcao_categorias])==1, '`proporcao_categorias` não soma 100%! Favor rever.'

    # garantir reprodutibilidade dos valores
    random.seed(seed)

    # Calcula o número de transações por categoria com base na proporção
    numero_transacoes_por_categoria = {categoria: int(num_transacoes * proporcao) for categoria, proporcao in proporcao_categorias.items()}
    
    transacoes = []
    
    # Gera as transações
    for categoria, quantidade in numero_transacoes_por_categoria.items():
        for _ in range(quantidade):
            transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": round(random.uniform(1.0, 1000.0), 2),  # Preço aleatório entre 1 e 1000
                "categoria": categoria
            }
            transacoes.append(transacao)
    
    return transacoes

def salvar_json(transacoes, path2save, filename):
    # create path if not exist
    if not os.path.exists(path2save):
        os.makedirs(path2save)
    with open(os.path.join(path2save,filename), "w") as file:
        json.dump(transacoes, file, indent=4)
    print(f"Arquivo salvo em: {os.path.abspath(os.path.curdir)+'/'+path2save+'/'+filename}")

def criar_bd(num_transacoes:int = 10000, proporcao_categorias:list = settings.categorias_proporcao, path2save="./data", filename='transactions.json'):
    salvar_json(criar_transacoes(num_transacoes,  proporcao_categorias),
                path2save, filename
    )

def load_bd(filepath='./data/transactions.json'):
    with open(filepath, "r") as file:
        bd = json.load(file)
    return bd

def tela_inicial():
    print("Bem-vindo <teu nome inteiro aqui>!")
    print('conta: 0000001-0')
    print("\nEste programa permite gerenciar transações de sua conta pessoal.")
    print("\nEscolha uma das opções abaixo:")
    print("1. Visualizar relatórios")
    print("2. Cadastrar transações")
    print("3. Editar transações")
    print("4. Excluir transações")
    print("-" * 10)
    print("0. Sair\n")

# -----------------------
# PROGRAM functions 
# -----------------------
# pode editar como quiser as funções abaixo! Somente não altere os nomes das funções.
# para alterar as funções abaixo, basta apagar o `pass` e preencher com as instruções.

def run():
    """
    Esta é a função principal que vai rodar o programa
    """
    
    # exibe a tela inicial
    tela_inicial()

    #input do usuario
    opcao = int(input('Digite uma opcao: ').strip())

    # visualizar relatorios
    if opcao==1:
        # limpar console (opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        visualizar_relatorios(bd)
    
    # sair
    if opcao==0:
        sys.exit()

def visualizar_relatorios(bd):
    """
    Mostra um menu de opcoes no qual gera relatórios com base na escolha do usuário.
    """
    print('Escolha um relatorio para ser visualizado:')
    print('\n1. Exibir soma total de transações')
    print('2. 5 transações mais caras')
    print('3. 5 transações medianas')
    print('4. 5 transações mais baratas')
    print('5. Exibir média total')
    print('6. Consultar transação por ID')
    print('-'*10)
    print('0. Voltar ao menu principal\n')

    #input do usuario
    opcao = int(input('Digite uma opcao: ').strip())

    if opcao==1:
        #limpar console (opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        calcular_total_transacoes(bd)
    
    if opcao==3:
        #limpar console (opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        calcular_media(bd)
    
    if opcao==0:
        #limpar console (opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        run()

def salvar_relatorio(texto_a_salvar):
    """
    Salvar o relatório gerado em .txt
    \nAplicar esta função em todos os relatórios listados em `visualizar_relatorios`
    """

def pegar_valores_bd_por_categoria(bd):
    # esta funcao vai pegar os valores do bd por categoria
    # Obter todos as categorias e agregar todos os valores nessas categorias
    transacoes_por_categoria = {}
    for transaction in bd:
        # verifica se uma key nao esta no dict de transacoes
        if transaction['categoria'] not in transacoes_por_categoria:
            # se nao estiver, adiciona
            transacoes_por_categoria[transaction['categoria']] = []
        # se ja tiver a key, adiciona o value
        else:
            transacoes_por_categoria[transaction['categoria']].append(transaction['preco'])
    
    return transacoes_por_categoria

def pegar_todos_os_valores(bd):
    todos_os_valores = map(lambda x: x['valor'],bd)
    return todos_os_valores

def calcular_total_transacoes(bd):
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """
    #soma total
    soma_total = sum(pegar_todos_os_valores(bd))
    # salva texto do relatório e exibe o texto
    relatorio = f"Soma total de transações: US$ {soma_total:.2f}"
    print(relatorio)

    opcao = input('\n-----\nDeseja salvar relatório ? (y/[n]): ').strip()

    if opcao=='y':
        salvar_relatorio(relatorio)
        opcao = 'n'

    if (opcao=='n') or (not opcao):
        #limpar console (opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        # rodar o menu principal
        run()


def mostrar_m5_transacoes():
    """
    Mostra as m5 transações realizadas, sendo m parâmetro que deve ser adicionada à função.
    \nm : 'max','min','median', sendo 
    \n\t'max' mostra os top 5 maior valor,
    \n\t'min' mostra os top 5 menor valor,
    \n\t'mean' mostra os top 5 valores próximos a média
    
    Utilize essa mesma função para o caso `por categoria`
    """

def calcular_media(por_categoria=False):
    """
    Calcula a média dos valores das transações.
    Utilize essa mesma função para o caso `por categoria`
    """
    # input: bando de dados `bd` e opcao por_categoria (padrao FALSE)

    # perguntar se o usuario quer por categoria e salvar numa variavel
    por_categoria = True if input('Deseja classificar por categoria? (y/[n])')=='y' else False

    # Se foi pedido por categoria:
    if por_categoria:
        transacoes_por_categoria = pegar_valores_bd_por_categoria(bd)
        media_por_categoria = {k:media for k,media in zip(transacoes_por_categoria.keys(), map(lambda x: sum(x)/len(x), transacoes_por_categoria.values()))}
        return media_por_categoria
    else:
        transacoes = pegar_todos_os_valores(bd)
        media_total = transacoes
        return media_total

def consultar_transacao_por_ID():
    """
    Consulta uma transação específica pelo seu UUID.
    """
    pass

def cadastrar_transacao():
    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """

def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """
    pass

def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """
    pass

# -----------------------
# MAIN SCRIPT
# -----------------------
# não alterar nada abaixo
if __name__ == "__main__":
    
    # -----------------------
    # NÃO ALTERAR ESTE BLOCO
    # -----------------------
    # criar o banco de dados caso ele não exista
    print(os.path.abspath('.'))
    if not os.path.exists('./data/transactions.json'):
        criar_bd()
    
    # load bd 
    bd = load_bd()
    # -----------------------

    # -----------------------
    # ABAIXO PODE ALTERAR
    # -----------------------
    #limpar console (opcional)
    os.system('cls' if os.name == 'nt' else 'clear')
    # inicia o programa
    run()