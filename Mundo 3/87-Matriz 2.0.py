matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista = []
soma = 0
soma3 = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {c}, {l}: '))

for i in range(0, 3):
    print(f'[{matriz[i][0]:^10}]', end='')
    print(f'[{matriz[i][1]:^10}]', end='')
    print(f'[{matriz[i][2]:^10}]\n', end='')

for l in matriz:
    for c in l:
        if c % 2 == 0:
            soma += c
print(f'A soma de todos foi {soma}')
    
for c3 in matriz:
    if c3[2] > 0:
        soma3 += c3[2]
print(f'A soma de todos da casa 2 é {soma3}')

print(f'O maior valor da segunda linha é {max(matriz[1])}.')
