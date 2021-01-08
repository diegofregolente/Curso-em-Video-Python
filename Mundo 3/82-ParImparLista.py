lista = list()
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if r in 's':
            break
        elif r in 'n':
            break
        elif r not in 's':
            print('Não entendi o que você quis dizer...', end='')
    if r in 'n':
        break

for n in lista:
    if n % 2 == 0:
        listaPar.append(n)
    elif n % 2 == 1:
        listaImpar.append(n)

print(f'A lista é: {lista}')
print(f'Pares: {listaPar}')
print(f'Impares: {listaImpar}')
