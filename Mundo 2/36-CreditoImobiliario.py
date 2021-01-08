casa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite o valor do seu salario? '))
anos = int(input('Quantos anos você seja pagar? '))
mensalidade = casa / (anos * 12)
minimo = salario*(30/100)
print(f'O valora da sua prestação é {mensalidade:.2f}, durante {anos*12} meses e o minimo que você pode pagar é {minimo:.2f}')
if minimo > salario:
    print('CRÉDITO NEGADO')
elif minimo <= salario:
    print('CREDITO APROVADO')
