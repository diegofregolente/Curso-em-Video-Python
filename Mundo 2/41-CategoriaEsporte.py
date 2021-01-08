anoNasc = int(input('Digite seu ano de nascimento: '))
idade = 2020 - anoNasc
if idade <= 9:
    print('Até 9 anos: MIRIN')
elif idade > 9 and idade <= 14:
    print('Até 14 anos: INFANTIL')
elif idade > 14 and idade <=19:
    print('Até 19 anos: JUNIOR')
elif idade == 20:
    print('Até 20 anos: SENIOR')
else:
    print('Acima de 20 anos: MASTER')
