primeiro = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = 10
while decimo > 0:
    print(primeiro, end=' ')
    primeiro += r
    decimo -= 1
p = int(input('\nPrecisa de mais termos: '))
while p != 0:
    print(primeiro, end=' ')
    primeiro += r
    p -= 1
    if p == 0:
        p = int(input('\nPrecisa de mais termos: '))
print('Acabou')