a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c
print(f'Menor é: {menor}')

maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c
print(f'Maior é: {maior}')
