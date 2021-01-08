peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura * altura)
print(f'Seu imc é {imc:.2f}')
if imc <= 18.5:
    print('Abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Peso Ideal.')
elif imc > 25 and imc <= 30:
    print('Sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
