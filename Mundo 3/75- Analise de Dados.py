tupla = (int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')))

print(f'Você digitou os valores {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if tupla.count(3) > 0:
    print(f'O primeiro 3 aparece na posição {tupla.index(3)}')
else:
    print('Não tem 3 na tupla')

print('Os numeros pares são: ', end='')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
