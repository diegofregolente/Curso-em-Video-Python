from random import randint
from time import sleep


def sorteio():
    print('Sorteando os 5 valores da lista: ', end='')
    for n in range(0, 5):
        n = randint(1, 9)
        numeros.append(n)
        print(n, end=' ', flush=True)
        sleep(0.4)
    print('FIM!')


def somaPar():
    somaP = 0
    for n in numeros:
        if n % 2 == 0:
            somaP += n
    print(f'Foram sorteados os numeros {numeros} e a soma dos pares foi {somaP}')


numeros = []
sorteio()
somaPar()
