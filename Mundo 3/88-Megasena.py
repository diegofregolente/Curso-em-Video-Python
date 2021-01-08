from random import randint
from time import sleep

tot = []
megasena = []

megasena_screen = 'JOGA NA MEGA!!!'
line = '-'*50
print(line)
print(f'{megasena_screen:^50}')
print(line)

jogo = int(input('Quantas vezes: '))

for j in range(jogo):
    while len(megasena) != 6:
        c = randint(1,61)
        if c in megasena:
            megasena.remove(c)
        elif c not in megasena:
            megasena.append(c)
            megasena.sort()
    tot.append(megasena[:])
    megasena.clear()

for i, j in enumerate(range(jogo)):
    print(f'Jogo {i+1}: {tot[j]}')
    sleep(0.5)
