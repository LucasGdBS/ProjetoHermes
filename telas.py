def registro(tipoAtendimento, setor, hotel, apto):
    print('='*30)

    print(f'{tipoAtendimento}')
    print(f'{setor}')
    print(f'{hotel}')
    print(f'{apto}')
    descricao = input('Descreva o seu problema:')

    return descricao

registro()