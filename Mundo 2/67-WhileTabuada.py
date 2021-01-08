n = 0
c = 0
while True:
    n = int(input('Você deseja ver a tabuada de qual numero? '))
    if n < 0:
        break
    for numero in range(1, 11):
        print(f'{n} x {numero} = {n*numero}')
print('ENCERRANDO...')