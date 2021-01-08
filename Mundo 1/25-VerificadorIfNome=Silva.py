nome = str(input('Digite o nome de uma pessoa: ')).strip().upper()
if 'SILVA' in nome:
    print(f'Esse nome tem silva, {nome}')
else:
    print(f'Esse nome não tem silva, {nome}')
exit()