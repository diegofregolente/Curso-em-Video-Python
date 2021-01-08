from time import sleep
qntMaior = 0
qntHomem = 0
qntMulher = 0
while True:
    nome = str(input('Digite um nome: ')).strip().lower()
    idade = int(input('Idade: '))
    if idade > 18:
        qntMaior += 1
    sexo = str(input('Qual sexo da pessoa? [M/F]: ')).strip().lower()[0]
    if sexo == 'm':
        qntHomem += 1
    elif sexo == 'f' and idade < 20:
        qntMulher += 1
    continua = str(input('Novo Cadastro? [S/N]: ')).strip().lower()[0]
    if continua != 's':
        break
print('Inserindo dados...')
sleep(1)
print('_'*20)
print(f'Temos {qntMaior} pessoas acima de 18 anos.')
print(f'Temos {qntHomem} homens cadastrados.')
{print(f'Temos {qntMulher} mulheres abaixo de 20 anos.')}
