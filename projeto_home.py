from time import sleep
import os
os.system("cls")

# Programa do Projeto Rede Chambres Hoteis

# cores
backg = ('\033[m',         # 0 - sem cores'
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;30',      # 6 - branco

         )

# Funções


def chambres(cor=0):  # Titulo
    os.system("cls")
    print(backg[1], end="")
    print('~'*100)
    hotel = " CHAMBRES HOTEIS "
    print(hotel.center(100, '~'))
    print('~'*100)
    print(backg[0], end="")
    sleep(1)


def menu_main(op):  # Função do Menu Principal
    print("Menu Principal : \n")
    op_menu_main = int(
        input(" 1 - Serviços \n 2 - Reclamações \n 3 - Sair  \n\nQual opção deseja acessar? "))
    return op_menu_main


def menu_servico(op2):  # Função do Menu Serviços
    print("Menu Serviços \n")
    op_menu_serv = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Status\n 6 - Voltar \n\nQual opção deseja acessar "))

    # opcao 1 - colocar outra funcao para acessar (if) cada opção
    return op_menu_serv


def menu_reclamacao(op3):  # Função do Menu Reclamações
    print("Menu Reclamações \n")
    op_menu_recl = int(input(
        " 1 - Recepção\n 2 - Manutenção\n 3 - Serviços Gerais\n 4 - Copa\n 5 - Status\n 6 - Voltar \n\nQual opção deseja acessar "))
    # opcao 1 - colocar outra funcao para acessar (if) cada opção
    return op_menu_recl


# Programa Principal
op_menu = 0
while (op_menu != 3):
    chambres()
    op_menu = menu_main(0)
    op_menu_serv = 0
    op_menu_reclamacao = 0
    atend = ""
    setor = ""

    if op_menu == 1:  # acesso ao menu de Serviço
        os.system("cls")
        chambres()
        menu_servico(0)
        if op_menu_serv == 1:
            atend = "Serviço"
            setor = "Recepção"
        elif op_menu_serv == 2:
            atend = "Serviço"
            setor = "Manutenção"
        elif op_menu_serv == 3:
            atend = "Serviço"
            setor = "Serviços Gerais"
        elif op_menu_serv == 4:
            atend = "Serviço"
            setor = "Copa"
        elif op_menu_serv == 5:
            atend = "Reclamação"
            setor = "Status"
        elif op_menu_serv == 6:
            chambres()
            op_menu = menu_main(0)
        else:
            print("Opção Inválida !")

    elif op_menu == 2:  # acesso ao menu de Reclamações
        os.system("cls")
        chambres()
        menu_reclamacao(0)
        if op_menu_serv == 1:  # Acessar a função de registro reclamações
            atend = "Reclamação"
            setor = "Recepção"
        elif op_menu_serv == 2:
            atend = "Reclamação"
            setor = "Manutenção"
        elif op_menu_serv == 3:
            atend = "Reclamação"
            setor = "Serviços Gerais"
        elif op_menu_serv == 4:
            atend = "Reclamação"
            setor = "Copa"
        elif op_menu_serv == 5:
            atend = "Reclamação"
            setor = "Status"
        elif op_menu_serv == 6:
            chambres()
            op_menu = menu_main(0)
        else:
            print("Opção Inválida !")

    elif op_menu == 3:  # saida do loop
        break
    else:
        print("Opção Inválida !")

    op_menu = 0
