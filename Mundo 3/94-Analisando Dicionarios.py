d1 = {}
l1 = []
media = 0
qntF = 0

while True:
    d1['nome'] = (str(input('Nome: ')))
    d1['idade'] = int(input('Digite sua idade: '))

    while True:
        d1['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if d1['sexo'] in 'MF':
            break
        print('Digite apenas M ou F.')
    l1.append(d1.copy())
    while True:
        r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print('Digite apenas S ou N.')
    if r in 'N':
        break


print('~'*40)
print(f'- O grupo tem {len(l1)} pessoas.')

for v in l1:
    media += v['idade']
media = media / len(d1)
print(f'- A média de idade é {media:.1f}')

print(f'- As mulheres cadastradas foram: ', end='')
for v in l1:
    if v['sexo'] in 'F':
        print(f'{v["nome"]}', end=' ')

print(f'\n- Lista de pessoas que estão acima da média: \n')

for e in l1:
    if e['idade'] >= media:
        for k, v in e.items():
            print(f'{k} = {v}; ', end='')
        print()

print(f'Fim do Programa')