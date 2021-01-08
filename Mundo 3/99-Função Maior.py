from random import randint
from time import sleep

def maior(q):
    numeros = list()
    if q != 0:
        print('Analisando os valores passados...')
        for n in range(0, q):
            numeros.append(randint(1, 9))
            print(numeros[n], end=' ', flush=True)
            sleep(0.3)
    if q == 0:
        numeros.append(0)
    print(f'Foram informados {q} valores ao todo.')
    print(f'O maior numero foi {q}.')
    print('-='*25)

maior(6)
maior(3)
maior(1)
maior(0)
