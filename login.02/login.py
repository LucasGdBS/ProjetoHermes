with open('dadosh1.txt') as f:
    datah1 = f.readlines()
with open('dadosh2.txt') as g:
    datah2 = g.readlines()
with open('dadosh3.txt') as h:
    datah3 = h.readlines()

import PySimpleGUI as sg

hoteis=['Saint Patrick Praia Hotel','Hotel Des Basques','Pousada Nossa Casa']

def validateCredentialsh1(user,password):
    for loginsAllowed in datah1:
        if user + ';' + password  == loginsAllowed.strip():
            return True
    return False
def validateCredentialsh2(user,password):
    for loginsAllowed in datah2:
        if user + ';' + password  == loginsAllowed.strip():
            return True
    return False
def validateCredentialsh3(user,password):
    for loginsAllowed in datah3:
        if user + ';' + password  == loginsAllowed.strip():
            return True
    return False


#começa na home
def homepage():
    sg.theme('LightBrown6')
    layout = [
        [sg.Text('Bem vindo a rede de Hoteis Chambrés')],
        [sg.Button('Escolher Hotel')]
    ]
    return sg.Window('Projeto Hermes',layout=layout,finalize=True,size=(300,200))
#escolhe o hotel    
def hotel():
    sg.theme('LightBrown6')
    layout = [
        [sg.Text('Selecione o Hotel')],
        [sg.Listbox(hoteis, size=(30, 4))],
        [sg.Button('Confirmar')]
    ]
    return sg.Window('Projeto Hermes',layout=layout,finalize=True,size=(300,200))
#comeca o login
def login():
    sg.theme('LightBrown6')
    layout = [
        [sg.Text('Usuário')],       
        [sg.Input(key='user')],
        [sg.Text('Senha')],
        [sg.Input(key='password')],
        [sg.Button('Voltar')],
        [sg.Button('Login')],
        [sg.Text('',key='verify')],  
    ]
    return sg.Window('Projeto Hermes',layout=layout,finalize=True,size=(300,200))    




tela1,tela2,tela3 = homepage(),None,None

while True:
    window,event,values = sg.read_all_windows()
    if window == tela1 and event == sg.WIN_CLOSED:
        break
    if window == tela1 and event == 'Escolher Hotel':
        tela2 = hotel()
        tela1.hide()
    if window == tela2 and event == sg.WIN_CLOSED:
        break
    if window == tela2 and event == 'Confirmar':
        tela3 = login()
        tela2.hide()
    if window == tela3 and event == sg.WIN_CLOSED:
        break
    if window == tela3 and event == 'Voltar':
        tela3.hide()
        tela2.un_hide()
    print(event)

    if event == 'Confirmar':
        selection = values[0]
        if selection:
            selectionHotel = selection[0]
    if window == tela3 and event == 'Login':
        user=values['user']
        password=values['password']

        if selectionHotel in hoteis:
            if selectionHotel == hoteis[0]:
                if validateCredentialsh1(user,password):
                    window['verify'].update('Login realizado com sucesso')
                else:
                    window['verify'].update('Senha ou usuário incorreto')
            if selectionHotel == hoteis[1]:
                if validateCredentialsh2(user,password):
                    window['verify'].update('Login realizado com sucesso')
                else:
                    window['verify'].update('Senha ou usuário incorreto')
            if selectionHotel == hoteis[2]:
                if validateCredentialsh3(user,password):
                    window['verify'].update('Login realizado com sucesso')
                else:
                    window['verify'].update('Senha ou usuário incorreto')
        else:
            window['verify'].update('Senha ou usuário incorreto')
