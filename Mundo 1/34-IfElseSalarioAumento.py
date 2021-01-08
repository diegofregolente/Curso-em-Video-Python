salario = float(input('Digite o salario de um funcionario: '))
if salario > 1250:
    aumento = salario * (10/100)
    print(f'O salario do funcionaro com um aumento de 10% é {aumento+salario:.2f}')
elif salario <= 1250:
    aumento = salario * (15/100)
    print(f'O salario do funcionaro com um aumento de 15% é {aumento+salario:.2f}')
