ano = int(input('Esse ano, é bissexto?: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')

