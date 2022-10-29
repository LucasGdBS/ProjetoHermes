def registro(tipoAtendimento, setor, hotel, apto):
    from time import sleep
    from os import system
    
    while True:
        print(f'Tipo de atendimento - {tipoAtendimento}')
        print(f'Setor - {setor}')
        print(f'Hotel - {hotel}')
        print(f'Apartamento - {apto}')
        descricao = input(f'Descrição da {tipoAtendimento}: ')
        op = int(input('[1]Salvar/t[2]Voltar '))

        if op == 1:
            system('cls')
            #função salvar
            print('ta salvo')
            break
            
        elif op == 2:
            system('cls')
            print('voltar para home Page')
            break


registro('Solicitação', 'Copa', 'Chambres', '702')