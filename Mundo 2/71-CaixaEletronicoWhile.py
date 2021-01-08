banco = 'BANCO NACIONAL'
notas = 'Notas Disponiveis: 50, 20, 10 e 1 R$'
print('='*100)
print(f'{banco:^100}')
print(f'{notas:^100}')
print('='*100)
valor = input('Quanto você quer sacar? ')
saque = int(valor)
c50 = c20 = c10 = c1 = 0
a50 = 50
a20 = 20
a10 = 10
a1 = 1
rest = 0
atual = 0
while True:
    if saque >= 50:
        atual = saque - a50
        c50 += 1
        saque = atual
    elif atual >= 20:
        atual = saque - a20
        c20 += 1
        saque = atual
    elif atual >= 10:
        atual = saque - a10
        c10 += 1
        saque = atual
    elif atual >= 1:
        atual = saque - a1
        c1 += 1
        saque = atual
    else:
        break
print('='*100)
print(f'Total de {c50} notas de 50.')
print(f'Total de {c20} notas de 20.')
print(f'Total de {c10} notas de 10.')
print(f'Total de {c1} notas de 1.')
print('='*100)
