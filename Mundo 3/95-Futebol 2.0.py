jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}: ')))
    jogador['total'] = sum[partidas]
    jogador['gols'] = partidas[:]
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Digite apenas Sim ou Não.')
    print('-' * 50)
    if resp in 'N':
        break
print('_'*25)
print('No. ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('_'*25)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('_'*25)
while True:
    dados = int(input(' Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(futebol):
        print(f' Não existe jogador com No. {dados}')
    else:
        print(f' LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}')
        for p, g in enumerate(time[dados]["gols"]):
            print(f' Na partida {p+1} ele fez {g} gols.')
    print('_' * 25)
print('FIM DO PROGRAMA')
