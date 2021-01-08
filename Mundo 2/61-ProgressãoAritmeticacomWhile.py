primeiro = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = 10
while decimo > 0:
    print(primeiro, end=' ')
    primeiro += r
    decimo -= 1
