from arquivo import *


print('CONTROLE DE CADASTRO DOS HOSPEDES!')
while True:
    op = int(input('Deseja cadastrar um novo usuario[1] ou deletar[2]? '))

    if op == 1:
        login = input('Digite o login para cadastro: ')
        senha = input('Digite a senha para cadastro: ')

        if not arquivo_existe():
            criarArquivo()

        try:
            cadastro(login, senha)
            print('Cadastro efetuado com sucesso')
        except:
            print('Houve algum erro no cadastro! Tente novamente mais tarde ou contate o suporte')
   
    elif op == 2:
        login = input('Digite o login para deletar: ')
        senha = input('Digite a senha para deletar: ')

        if validacao(login, senha):
            deletar(login, senha)
            print('Deletado com sucesso!')
        else:
            print('Login e senha não encontrados!')
   
    else:
        print('Opção invalida, tente de novo!')