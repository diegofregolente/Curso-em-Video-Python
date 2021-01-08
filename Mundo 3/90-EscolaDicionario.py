escola = {}
escola['nome'] = str(input('Nome: '))
escola['média'] = float(input(f'Digite a média de {escola["nome"]}: '))
if escola['média'] < 5:
    escola['situacao'] = 'reprovado'
elif 5 <= escola['média'] < 7:
    escola['situacao'] = 'recuperacao'
else:
    escola['situacao'] = 'aprovado'
print(f'Nome de aluno é {escola["nome"]}')
print(f'Sua média foi de {escola["média"]:.2f}')
print(f'Sua situação é {escola["situacao"]}')
