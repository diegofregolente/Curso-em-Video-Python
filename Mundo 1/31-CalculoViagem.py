viagem = int(input('Quantos KM é a sua viagem: '))
if viagem <= 200:
    preco = viagem * 0.50
    print(f'Você vai ter que pagar {preco:.2f} R$')
elif viagem > 200:
    preco = viagem * 0.45
    print(f'Você vai ter que pagar {preco:.2f} R$')
