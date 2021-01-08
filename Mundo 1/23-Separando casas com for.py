num = str(input('Digite um numero de 0 a 9999: '))
if len(num) > 4:
    print('Você colocou um valor acima do permitido.')
    exit()
lista = []
for n in num:
    lista.append(n)
if len(lista) >= 0:
    print(f'Unidade: {lista[-1]}')
if len(lista) > 1:
    print(f'Dezena: {lista[-2]}')
if len(lista) > 2:
    print(f'Centena: {lista[-3]}')
if len(lista) > 3:
    print(f'Milhar: {lista[-4]}')
