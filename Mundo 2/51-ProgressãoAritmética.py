primeiro = int(input('PA: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(primeiro, end=' > ')
    primeiro += r
print('FIM')

# primeiro + (10 - 1) * razão | formula pra calcular temos de PA.