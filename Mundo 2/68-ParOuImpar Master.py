import random
c = 0
while True:
    parouimpar = ['par', 'impar']
    jogador = str(input('Par ou impar? ')).strip().lower()
    while jogador != parouimpar[0] and jogador != parouimpar[1]:
        jogador = str(input('Você não escolheu as opções corretas, tente novamente.\nPar ou impar? ')).strip().lower()
    computador = random.randint(0,10)
    n1 = int(input('Jogada de 0 a 10: '))
    while n1 > 10 or n1 < 0:
        print('Tá trollando?')
        n1 = int(input('Jogada de 0 a 10: '))
    if jogador == parouimpar[0] and (n1 + computador) % 2 == 0:
        print('Jogador Venceu')
        print(f'Jogador jogou {n1} e o computador {computador}')
        c += 1
    elif jogador == parouimpar[1] and (n1 + computador) % 2 == 1:
        print('Jogador Venceu')
        print(f'Jogador jogou {n1} e o computador {computador}')
        c += 1
    else:
        break
print(f'Jogador jogou {n1} e o computador {computador}')
print(f'O jogador ganhou {c} vezes.')

