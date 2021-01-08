menu = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while menu != 5:
    menu = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa\n'))
    if menu == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif menu == 2:
        multiplicar = n1 * n2
        print(f'{n1} * {n2} = {multiplicar}')
    elif menu == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero é {maior}')
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE.\n')
