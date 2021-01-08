import random
from time import sleep
jokenpo = str(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] Tesoura
Qual é a sua jogada? '''))
itens = ['Pedra','Papel','Tesoura']
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
if jokenpo == '0':
    usuario = itens[0]
    computador = random.choice(itens)
    print(f'Computador jogou {computador}\nJogador jogou {usuario}')
    if computador == 'Pedra':
        print('EMPATE!')
    elif computador == 'Papel':
        print('COMPUTADOR VENCE')
    elif computador == 'Tesoura':
        print('JOGADOR VENCE')
elif jokenpo == '1':
    usuario = itens[1]
    computador = random.choice(itens)
    print(f'Computador jogou {computador}\nJogador jogou {usuario}')
    if computador == 'Pedra':
        print('JOGADOR VENCE!')
    elif computador == 'Papel':
        print('EMPATE')
    elif computador == 'Tesoura':
        print('COMPUTADOR VENCE')
elif jokenpo == '2':
    usuario = itens[2]
    computador = random.choice(itens)
    print(f'Computador jogou {computador}\nJogador jogou {usuario}')
    if computador == 'Pedra':
        print('COMPUTADOR VENCE')
    elif computador == 'Papel':
        print('JOGADOR VENCE')
    elif computador == 'Tesoura':
        print('EMPATE')
else:
    print('JOGADA INVALIDA')