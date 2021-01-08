dias = int(input('Quantos dias foram alugados? '))
km = int(input('Quantos KMs foram rodados? '))
pagar = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de {pagar:.2f} R$')