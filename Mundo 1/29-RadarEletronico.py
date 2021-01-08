import random
velocidade = random.randint(60, 100)
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado por andar a {velocidade}, e vai ter que pagar {multa:.2f} R$')
else:
    print(f'Você está dentro da velocidade da pista, sua velocidade é {velocidade} .')
