def leiaint(n):
    while not n.isnumeric():
        print('\033[0:31mERRO! Digite um número inteiro válido.')
        n = input('\033[mDigite um numero: ')
    if n.isnumeric():
        int(n)
    print(f'Você digitou o {n}, fim do programa.')


leiaint(input('Digite um numero: '))