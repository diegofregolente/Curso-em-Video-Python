listaGeral = [[],[]]
for i in range(0, 7):
    n = int(input(f'Digite o numero {i}: '))
    if n % 2 == 0:
        listaGeral[0].append(n)
    else:
        listaGeral[1].append(n)

print(f'Os valores pares foram {sorted(listaGeral[0])}')
print(f'Os valores impares foram {sorted(listaGeral[1])}')