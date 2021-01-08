r = 'S'
c = 0
s = 0
maior = 0
menor = 0
while r == 'S':
    numero = int(input('Digite um numero: '))
    if c == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    c += 1
    s += numero
    m = s / c
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
print(f'A média de {c} numeros digitados foi {m:.1f}')
print(f'O menor numero foi {menor}')
print(f'O maior numero foi {maior}')
