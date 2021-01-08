numero = 0
c = 0
s = 0
numero = int(input('Digite um numero: '))
while numero != 999:
    s += numero
    c += 1
    numero = int(input('Digite um numero: '))
print(f'Foram digitados {c} e a soma deles foi {s}')