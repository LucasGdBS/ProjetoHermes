def gerarProtocolo(): #Função para gerar um numero de protocolo
    import datetime
    from random import randint

    dia = datetime.date.today().day
    mes = datetime.date.today().month
    ano = datetime.date.today().year

    while True:
        numero = randint(1000, 9999)
        protocol = f'{dia}{mes}{ano}{numero}'
        if not verificarProt(protocol):
            return protocol

def verificarProt(protocolo, nomeArq = 'registro.txt'): #Função que verifica se o protocolo ja existe
    if arquivo_existe():
        a = open(nomeArq, 'r')
        nProtocol = a.readlines()
        a.close()
        for i in range(len(nProtocol)):
            if protocolo in nProtocol[i].split(';'):
                return True
        return False

def confirmacao(tipoAtendimento, protocolo): #Função que mostra a mensagem dizendo que o atendimento foi registrado
    print(f'Sua {tipoAtendimento} foi registrada!\nO numero do protocolo é {protocolo}\nPara consulta clique em status no menu!')

def arquivo_existe(nome='registro.txt'): # Função para verificar se o arquivo já existe
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome='registro.txt'): #Função para criar o arquivo
    a = open(nome, 'w')
    a.close()

def salvarRegistro(protocolo, tipoAtendimento, setor, hotel, apto, descricao, nomeArquivo = 'registro.txt'): #Função que salva o atendimento no bloco de notas
    from time import sleep
    
    if not arquivo_existe():
        criar_arquivo()

    arquivo = open(nomeArquivo, 'a')
    arquivo.write(f'{protocolo}; {tipoAtendimento}; {setor}; {hotel}; {apto}; {descricao}\n')
    arquivo.close()

    confirmacao(tipoAtendimento, protocolo)
    sleep(4)
    return 0
