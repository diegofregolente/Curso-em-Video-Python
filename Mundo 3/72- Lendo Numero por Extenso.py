tupla = ('Zero','Um','Dois','Tres','Quatro','Cinco')

while True:
    while True:
        num = int(input('Digite um numero de 0 a 5: '))
        if num >= 0 and num <= 5:
            print(f'O numero {num} por extenso é {tupla[num]}.')
            break
        else:
            print('Numero não é 0 a 5.', end=' ')
    r = str(input('Quer continuar ? [S/N]: ')).upper()
    if r in 'N':
        break
print('Saindo...')
