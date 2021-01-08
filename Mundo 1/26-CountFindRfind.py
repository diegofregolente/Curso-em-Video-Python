frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra A:', frase.count('A'))
print(f'Quando aparece a primeira letra A:', frase.find('A'))
print(f'Quando aparece a ultima letra A:', frase.rfind('A'))
