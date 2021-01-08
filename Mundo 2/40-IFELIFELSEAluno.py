b1 = float(input('Digite a nota da primeira prova: '))
b2 = float(input('Digite a nota da segunda prova: '))
media = (b1+b2)/2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
