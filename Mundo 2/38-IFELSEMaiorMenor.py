a = int(input('Primeiro numero: '))
b = int(input('Segundo Numero: '))
if a > b:
    print(f'O maior numero é o primeiro. {a}')
elif b > a:
    print(f'O maior numero é o segundo. {b}')
else:
    print(f'Os dois numeros são iguais. {a} {b}')
