import random
computador = random.randint(0,10)
jogador = int(input('Digite um numero de 0 a 10: '))
tentativas = 0
while jogador != computador:
    jogador = int(input('Você errou, tente novamente: '))
    tentativas += 1
print(f'O jogador descobriu o numero {computador} e preciso de {tentativas} tentativas.')
