sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos, digite seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} inserido com sucesso.')
