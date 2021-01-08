from datetime import datetime
dados = {}

dados['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - anoNasc
dados['ctps'] = int(input('Carteiro de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('_'*35)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')