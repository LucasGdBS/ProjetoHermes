from time import sleep
import os
os.system("cls")

def chambres():  # Titulo
    os.system("cls")
    print(f'\033[31m', end="")
    print('~'*100)
    hotel = " CHAMBRES HOTEIS "
    print(hotel.center(100, '~'))
    print('~'*100)
    print(f'\033[m', end="")
    sleep(1)


def menu_main():  # Função do Menu Principal
    print("Menu Principal : \n")
    op_menu_main = int(
        input(" 1 - Serviços \n 2 - Reclamações \n 3 - Sair  \n\nQual opção deseja acessar? "))
    
    return op_menu_main


def menu_servico():  # Função do Menu Serviços
    print("Menu Serviços \n")
    op_menu_serv = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Status\n 6 - Voltar \n\nQual opção deseja acessar "))

    # opcao 1 - colocar outra funcao para acessar (if) cada opção
    return op_menu_serv


def menu_reclamacao():  # Função do Menu Reclamações
    print("Menu Reclamações \n")
    op_menu_recl = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Status\n 6 - Voltar \n\nQual opção deseja acessar "))
    # opcao 1 - colocar outra funcao para acessar (if) cada opção

    return op_menu_recl


def registro(tipoAtendimento, setor, hotel, apto): # Função para a tela de registro
    print('='*30)

    print(f'{tipoAtendimento}')
    print(f'{setor}')
    print(f'{hotel}')
    print(f'{apto}')
    descricao = input('Descreva o seu problema:')

    return descricao

