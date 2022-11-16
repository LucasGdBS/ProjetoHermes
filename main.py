#Importar os módulos aqui!
from SalvarRegistro import *
from status import *
from telas import *

# Escrever código aqui!
def inicio():
    chambres()
    hotel = escolhaHotel() #Seleção do hotel
    if telaLogin():
        mainMenu(hotelEscolhido=hotel)

def mainMenu(hotelEscolhido):
    while True:
        op = menu_main('Usuário', 111, hotelEscolhido)
        if op == 1:
            setor = menu_servico()
            tipoAtendimento = 'Serviços'
            break
        elif op == 2:
            setor = menu_reclamacao()
            tipoAtendimento = 'Opinião'
            break
        elif op == 3:
            op = status()
            if op == 1:
                mainMenu(hotelEscolhido)
            elif op == 2:
                feedBack()
                mainMenu(hotelEscolhido)
            
        elif op == 4:
            if tela_sobre_nos() == 1:
                mainMenu(hotelEscolhido)
        elif op == 5:
            if tela_contatos() == 1:
                mainMenu(hotelEscolhido)
        elif op == 6:
            inicio()
        else:
            print('Opção inválida, tente novamente!')
            sleep(2)
    
    descricao = registro(tipoAtendimento, setor, hotelEscolhido, 111)
    if descricao == 'Voltar':
        mainMenu(hotelEscolhido)
    else:
        salvarRegistro(gerarProtocolo(), tipoAtendimento, setor, hotelEscolhido, 111, descricao)
        mainMenu(hotelEscolhido)

inicio()
