from time import sleep

tot = 0
p1 = 0
nomeMaisBarato = ''
precoMaisBarato = 0
nome = ''
preco = ''

while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    while not nome.isalpha():
        nome = str(input('Digite o nome do produto: ')).strip()

    while not preco.isnumeric():
        preco = input('Digite o preço do produto R$: ').strip()
    preco = float(preco)

    if preco > 1000:
        p1 += 1
    while True:
        if precoMaisBarato == 0:
            precoMaisBarato = preco
            nomeMaisBarato = nome
            break
        elif preco < precoMaisBarato:
            precoMaisBarato = preco
            nomeMaisBarato = nome
            break
        else:
            break
    tot += preco

    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont in 'N':
        break

    preco = 'a'

sleep(0.5)
print('CALCULANDO DADOS INSERIDOS...')
sleep(0.5)
print('_' * 40)
print(f'Total de gastos foi de {tot} R$')
print(f'{p1} são acima de 1000 R$')
print(f'O produto mais barato foi {nomeMaisBarato}')
