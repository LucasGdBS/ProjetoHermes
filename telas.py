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
    #sleep(1)


def menu_main(nome, apto, hotel):  # Função do Menu Principal
    chambres()
    print("Menu Principal : \n")
    print(f'{nome}\n{hotel}\napto: {apto}\n')
    op_menu_main = int(
        input(" 1 - Serviços \n 2 - FeedBacks \n 3 - Status de solicitação \n 4 - Sobre nós \n 5 - Contatos \n 6 - Sair \n\nQual opção deseja acessar? "))
    
    return op_menu_main


def menu_servico():  # Função do Menu Serviços
    chambres()
    opcoes = {1:'Recepção', 2:'Manutenção', 3:'Serviçoes Gerais', 4:'Copa', 5:'Voltar'}

    print("Menu Serviços \n")
    op_menu_serv = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Voltar \n\nQual opção deseja acessar "))
    op_menu_serv = opcoes[op_menu_serv]

    # opcao 1 - colocar outra funcao para acessar (if) cada opção
    return op_menu_serv


def menu_reclamacao():  # Função do Menu Reclamações
    chambres()
    opcoes = {1:'Recepção', 2:'Manutenção', 3:'Serviçoes Gerais', 4:'Copa', 5:'Voltar'}

    print("Menu FeedBack\n")
    op_menu_recl = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Voltar \n\nQual opção deseja acessar "))
    
    op_menu_recl = opcoes[op_menu_recl]    

    return op_menu_recl


def registro(tipoAtendimento, setor, hotel, apto): # Função para a tela de registro
    chambres()
    print(f'Tipo do atendimento: {tipoAtendimento}\n')
    print(f'Setor: {setor}\n')
    print(f'Hotel: {hotel}\n')
    print(f'Apto: {apto}\n')
    descricao = input('Descreva o seu problema:')
    op = int(input('[1] Salvar solicitação\t[2] Voltar '))
    
    if op == 1:
        return descricao
    else:
        descricao = 'voltar'
        return descricao

def feedBack(): # Tela para feedBack
    nota = int(input('Digite uma nota de 0 a 5: '))
    if nota >= 4:
        print('Ficamos felizes em saber que conseguimos atender suas expectativas!')
    else:
        print('Sentimos muito... esperamos poder melhorar e lhe atender melhor')
    sleep(4)

def telaLogin():
    while True:
        chambres()
        login = input('Digite seu apartamento: ')
        senha = input('Digite sua senha: ')

        if f'{login};{senha}' == f'702;123456789':
            return True
        else:
            print('login invalido, tente novamente')
            sleep(1)

def escolhaHotel():
    while True:
        chambres()
        hotel = int(input('Hoteis\n[1]Saint Patrick Praia Hotel\n[2]Hotel Des Basques\n[3]Pousada Nossa Casa\nEscolha o hotel em que se encontra:'))
        if hotel == 1:
            hotel = 'Saint Patrick Praia Hotel'
            return hotel
        elif hotel == 2:
            hotel = 'Hotel Des Basques'
            return hotel
        elif hotel == 3:
            hotel = 'Pousada Nossa Casa'
            return hotel
        else:
            print('Opção não valida, tente novamente')
            sleep(1)

def tela_contatos():
    print("\nTelefone: +55 (82) 3325-7785\n\nInstagram: <https://www.instagram.com/chambreshoteis/>\n\nFacebook: <https://www.facebook.com/chambreshoteis>\n")
    op = int(input('1 - Voltar: '))
    return op

def tela_sobre_nos():
    print("\nNossa missão é conectar pessoas a experiências\nincríveis, criar laços e promover o bem-estar.")
    print("\nSomos aquilo que amamos, viagem, conforto e hospitalidade")
    print("\nEstamos presentes em Maceio/AL desde 1991.\nNossos hoteis ficam em localizações estrategicas\npara voce se sentir perto de tudo que precisar.\n")
    op = int(input('1 - Voltar: '))
    return op



