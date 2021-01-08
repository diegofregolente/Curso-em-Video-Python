n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print(f'{n} foi divisivel {cont} vezes, por isso é primo')
else:
    print(f'{n} foi divisivel {cont} vezes, por isso não é primo')
