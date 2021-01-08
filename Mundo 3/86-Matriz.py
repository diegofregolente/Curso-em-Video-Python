matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista = []

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {c}, {l}: '))

for i in range(0, 3):
    print(f'[{matriz[i][0]:^10}]', end='')
    print(f'[{matriz[i][1]:^10}]', end='')
    print(f'[{matriz[i][2]:^10}]\n', end='')

