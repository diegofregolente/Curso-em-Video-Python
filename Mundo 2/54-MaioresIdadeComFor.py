c = 0
co = 0
for pessoa in range(1, 8):
    anoNasc = int(input(f'Digite o ano de nascimento da pessoa {pessoa}: '))
    if 2020 - anoNasc < 18:
        c += 1
    elif 2020 - anoNasc >= 18:
        co += 1
print(f'{c} pessoas são menores de idade e {co} são maiores de idade.')
