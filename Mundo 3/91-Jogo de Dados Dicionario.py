from random import randint

dado = {'Jogador 1':randint(1, 6),'Jogador 2':randint(1, 6),
        'Jogador 3':randint(1, 6),'Jogador 4':randint(1, 6)}

print('Os valores sorteados foram:')
for k, v in dado.items():
    print(f'    O {k} tirou o numero {v}')

c = 1
print('Ranking: ')
for k, v in sorted(dado.items(), reverse=True, key=lambda item: item[1]):
    print(f'    {c}° foi de {k} obteve {v}')
    c += 1
