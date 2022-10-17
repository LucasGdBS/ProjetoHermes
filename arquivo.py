def arquivo_existe(nome='registro.txt'):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome='registro.txt'):
    a = open(nome, 'w')
    a.close

def cadastro(login, senha, nome='registro.txt'):
    a = open(nome, 'a')
    a.write(f'{login};{senha}\n')
    a.close

def validacao(login, senha, nome='registro.txt'):
    a = open(nome, 'r')
    ret = f'{login};{senha}\n'
    if ret in a:
        a.close()
        return True
    else:
        a.close()
        return False

def deletar(login, senha, nome='registro.txt'):
    ret = f'{login};{senha}\n'
    print(f'ret - {ret}')

    a = open(nome, 'r')
    linhas = a.readlines()
    linhas.pop(linhas.index(ret))
    a.close

    a = open(nome, 'w')
    a.writelines(linhas)
    a.close()

