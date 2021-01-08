futebol = {}
gols = []

futebol['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))

for k in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {k+1}: ')))

futebol['gols'] = gols
futebol['total'] = sum(gols)

print('~'*35)

for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')

print('~'*35)

print(f'O jogador {futebol["nome"]} jogou {partidas} partidas')

for c, v in enumerate(futebol['gols']):
    print(f'Na partida {c+1}, fez {v} gols.')

print(f'Foi um total de {futebol["total"]}')