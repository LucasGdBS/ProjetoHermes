from SalvarRegistro import *
from tabulate import tabulate


def lerArquivo(nomeArquivo = 'registro.txt'):

    global listas 
    listas = []
    table = []

    if arquivo_existe():
        a = open(nomeArquivo, 'r')
        linhas = a.readlines()
        for i in range(len(linhas)):
            listas.append(linhas[i].split('; '))
        for i in range(len(listas)):
            table.append([str(i+1), listas[i][0], listas[i][1], listas[i][2], listas[i][3], 'Em analise'])
            # str(i+1) Numero
            # listas[i][0] Protocolo
            # listas[i][1] Categoria
            # listas[i][2] Setor
            # Em analise Status

        return table

def ampliar():
    op = input('Digite o número da solicitação que deseja ampliar: ')
    lista = lerArquivo()
    try:
        for i in range(len(lista)):
            if op in lista[i]:
                print(f'Numero de Protocolo: {listas[i][0]}')
                print(f'Tipo de atendimento: {listas[i][1]}')
                print(f'Setor: {listas[i][2]}')
                print(f'Status de andamento: Em analise')
                print(f'Descrição: {listas[i][5]}')
                return True
    except TypeError:
        print('Nenhuma solicitação com esse número encontrado')

def tabular(cabecalho = ['Número', 'Protocolo', 'Categoria', 'Setor', 'Hotel', 'Status de andamento'], tabela = lerArquivo()):
    cabecalho = ['Número', 'Protocolo', 'Categoria', 'Setor', 'Hotel', 'Status de andamento']
    print(tabulate(tabela, headers=cabecalho, tablefmt='fancy_grid'))

def status():
    tabular()
    if ampliar():
        op = int(input('[1]Voltar\t[2]FeedBack'))
    else:
        op = int(input('[1]Voltar'))

    return op

status()

