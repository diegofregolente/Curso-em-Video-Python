inverso = ''
frase = str(input('Digite um frase: ')).strip().lower().replace(' ','')
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo.')
