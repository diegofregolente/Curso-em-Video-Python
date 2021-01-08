salario = float(input('Quanto é o salário do funcionário? R$ '))
aumento = salario * (15/100)
salarioFinal = salario + aumento
print(f'Com o aumento de {aumento:.2f} o salário do funcionário foi para {salarioFinal:.2f} R$')