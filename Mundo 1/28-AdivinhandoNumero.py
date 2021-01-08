import random
numero = random.randint (0, 5)
resposta = int(input('Qual numero eu estou pensando? '))
if numero == resposta:
    print(f'Como você sabia que eu estava pensando no {numero}')
else:
    print(f'Você errou! o numero que eu estou pensando é {numero}')
