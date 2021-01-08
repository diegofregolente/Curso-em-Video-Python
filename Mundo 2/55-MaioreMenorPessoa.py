maior = 0
menor = 0
for pessoa in range(0, 5):
    peso = float(input(f'Quantos kg a pessoa {pessoa+1} pesa? '))
    if pessoa == 0:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'A pessoa com menor peso foi a {menor} e a maior {maior}')
