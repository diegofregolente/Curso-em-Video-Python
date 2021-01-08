lista = []

for numero in range(0,5):
    lista.append(int(input(f'Digite o numero da posição {numero}: '))) # criando a lista

print(f'Minha lista tem os seguintes numeros {lista}') # mostrando a lista

print(f'O maior valor da lista é {max(lista)} na posição ', end='') # mostrando o maior e sua posição
for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p} ', end='')

print() # pulando linha por causa do end

print(f'O menor valor da lista é {min(lista)} na posição ', end='') # mostrando o menor e sua posição
for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p} ', end='')
