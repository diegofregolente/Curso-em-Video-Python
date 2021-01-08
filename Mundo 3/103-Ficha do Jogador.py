def ficha(nome, gols):
    if nome.isnumeric() or gols.isalpha():
        print('Dados Invalidos.')
    else:
        if not nome:
            nome = '<desconhecido>'
        if not gols:
            gols = 0
        print('-' * 40)
        print(f'O jogador {nome} fez {gols} gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))

ficha(nome, gols)
