lista = [] # lista vazia
while True:
    valor = int(input('Digite um valor: ')) # lendo 1 valor

    if valor not in lista:
        lista.append(valor) # se o valor não estiver na lista ainda, inserir.
        print('Valor Adicionar')

    elif valor in lista: # se ele estiver, não fazer nada.
        print('Valor Duplicado, não será inserido..')

    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if r in 's':
            break
        elif r in 'n':
            break
        elif r not in 's':
            print('Não entendi o que você quis dizer...', end='')
    if r in 'n':
        break
print(f'Foram digitados os valores {lista}') # mostre a lista

