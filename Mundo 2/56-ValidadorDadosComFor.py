somaIdade = 0
idadeMaior = 0
nomeMaior = ''
c = 0
for cadastro in range(0, 4):
        nome = str(input('Digite seu nome: ')).strip()
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
        somaIdade += idade
        mediaIdade = somaIdade / 4
        if idade > idadeMaior and sexo == 'M':
                idadeMaior = idade
                nomeMaior = nome
        if sexo == 'F' and  idade < 20:
            c += 1
print(f'A média de idade do grupo é {mediaIdade:.0f}')
print(f'A idade do homem mais velho é {nomeMaior}')
print(f'A quantidade de mulheres abaixo dos é {c}')
