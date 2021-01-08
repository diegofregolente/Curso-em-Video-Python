lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if r == 's':
            break
        elif r == 'n':
            break
        elif r not in 's':
            print('Não entendi o que você quis dizer...', end='')
    if r in 'n':
        break

print(f'\nVocê digitou {len(lista)} elementos.')

lista.reverse()
print(f'Os valores em ordem decrescente são {lista}')

if lista.count(5) > 0:
    print('Tem 5 na lista.')
else:
    print('Não tem 5 na lista.')
