def gerarProtocolo():
    import datetime
    from random import randint
    
    dia = datetime.date.today().day
    mes = datetime.date.today().month
    ano = datetime.date.today().year

    numero = randint(1000, 9999)
    protocol = f'{dia}{mes}{ano}{numero}'

    return protocol

def confirmacao(tipoAtendimento, protocolo):
    print(f'Sua {tipoAtendimento} foi registrada!\nO numero do protocolo é {protocolo}\nPara consulta clique em status no menu!')

def arquivo_existe(nome='registro.txt'):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome='registro.txt'):
    a = open(nome, 'w')
    a.close()

def salvarRegistro(protocolo, tipoAtendimento, setor, hotel, apto, descricao, nomeArquivo = 'registro.txt'):
    from time import sleep
    
    if not arquivo_existe():
        criar_arquivo()
    
    registro = [protocolo, tipoAtendimento, setor, hotel, apto, descricao]

    arquivo = open(nomeArquivo, 'a')
    arquivo.write(f'Protocolo: {protocolo}, Tipo Atendimento: {tipoAtendimento}, Setor: {setor}, Hotel: {hotel}, Apto: {apto}, Descriçaõ: {descricao}\n')
    arquivo.close()

    confirmacao(tipoAtendimento, protocolo)
    sleep(2)
    print('HOME') #Vai trocar depois


#main
descricao = 'Mofo na parede'
salvarRegistro(gerarProtocolo(), 'Reclamação', 'copa', 'San patrick', 702, descricao)
