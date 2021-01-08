dados = [] # lista de dados a serem inseridos
geral = [] # lista onde vamos inserir os dados solicitados
maior = menor = 0 # variaveis para identificar maiores e menores

while True:
    dados.append(str(input('Nome: '))) # insira o primeiro dado da lista [0]
    dados.append(float(input('Peso: '))) # insira o primeiro dado da lista [0]
    geral.append(dados[:]) # faça uma copia de dados [0] [1] para geral com o [:]
    dados.clear() # limpe a lista dados.
    while True: # while Validando se vc quer continuar, analisando se foi digitando s, n, ou outra letra.
        r = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if r in 's':
            break
        elif r in 'n':
            break
        elif r not in 's':
            print('Não entendi o que você quis dizer...', end='')
    if r in 'n':
        break

print(f'Cadastros: {len(geral)}') # mostrando quantas listas foram inseridos em geral

for pos, g in enumerate(geral): # analisando verificando qual foi o maior e menor peso da lista
    if pos == 0:
        maior = menor = g[1]
    elif g[1] > maior:
        maior = g[1]
    elif g[1] < menor:
        menor = g[1]

print(f'O maior peso foi {maior:.2f} KG, Peso de  ', end='')
for pessoas in geral: # se o peso de pessoas[1] for == ao do maior insiraa os nomes pessoas[0] um atras do outro
    if pessoas[1] == maior:
        print(f'{pessoas[0]}', end=' ')

print(f'\nO menor peso foi {menor:.2f} KG, Peso de  ', end='')
for pessoas in geral: # se o peso de pessoas[1] for == ao do menor insira os nomes de pessoas[0] um atras do outro
    if pessoas[1] == menor:
        print(f'{pessoas[0]}', end=' ')
