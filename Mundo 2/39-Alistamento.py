ano = int(input('Digite seu ano de nascimento: '))
idade = 2020 - ano
print(f'Sua idade é {idade}')
if idade > 18:
    atraso = idade - 18
    print(f'Passou do tempo de se alistar, você esta {atraso} anos atrasado')
elif idade == 18:
    print(f'Hora de se alistar! Você tem {idade} anos')
else:
    alistamento = 18 - idade
    print(f'Você ainda vai se alistar, falta {alistamento} anos para você se alistar.')
