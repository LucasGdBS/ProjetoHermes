from SalvarRegistro import *
from tabulate import tabulate
from telas import chambres


def lerArquivo(nomeArquivo = 'registro.txt'):

    global listas 
    listas = []
    table = []

    if arquivo_existe():
        a = open(nomeArquivo, 'r')
        linhas = a.readlines()
        a.close()
        for i in range(len(linhas)):
            listas.append(linhas[i].split('; '))
        for i in range(len(listas)):
            table.append([str(i+1), listas[i][0], listas[i][1], listas[i][2], listas[i][3], 'Em análise'])
            # str(i+1) Numero
            # listas[i][0] Protocolo
            # listas[i][1] Categoria
            # listas[i][2] Setor
            # Em analise Status
        return table

def ampliar():
    while True:
        op = input('Digite o número da solicitação que deseja visualizar. Digite [-1] para Voltar: ')
        if op != '-1':
            lista = lerArquivo()
            try:
                for i in range(len(lista)):
                    if op in lista[i]:
                        chambres()
                        print(f'Número de Protocolo: {listas[i][0]}')
                        print(f'Tipo de atendimento: {listas[i][1]}')
                        print(f'Setor: {listas[i][2]}')
                        print(f'Status de andamento: Em análise')
                        print(f'Descrição: {listas[i][5]}')
                        return True
            except:
                print('Não há registro com este número de protocolo.')
        else:
            return False


def tabular(cabecalho = ['Número', 'Protocolo', 'Categoria', 'Setor', 'Hotel', 'Status de andamento']):
    cabecalho = ['Número', 'Protocolo', 'Categoria', 'Setor', 'Hotel', 'Status de andamento']
    print(tabulate(lerArquivo(), headers=cabecalho, tablefmt='fancy_grid'))

def status():
    chambres()
    tabular()
    if ampliar():
        op = int(input('[1]Voltar\t[2]FeedBack: '))
    else:
        op = 1

    return op

#status()

