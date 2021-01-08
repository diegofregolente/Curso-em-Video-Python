lista = list() # lista vazia

for pos, num in enumerate(range(0,5)): # gerando 5 casa e 5 numeros com interação com o usuário
    num = int(input('Digite um valor: '))
    if pos == 0 or num > max(lista): # se o numero for a primeira ocorrencia (0) ou maior que o max da lista inserir no fim.
        lista.append(num)
        print('Numero inserido no final da lista.')

    else:
        pos = 0 # posição = 0 para começar a varrer a lista
        while pos < len(lista): # enquanto a pos não chegar na quantidade de casas da lista
            if num <= lista[pos]: # se o num inserido for menor ou igual = lista [ posição atual ]
                lista.insert(pos, num) # insira na posição atual o numero digitado
                print(f'O {num} foi inserido na casa {pos}')
                break # encerra
            pos += 1 # soma += 1 se não tiver atingindo o break

print(lista) # mostre a lista ordenada sem sort