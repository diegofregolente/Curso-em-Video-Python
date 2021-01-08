tupla = ('python','programacao','programador','aprendendo')
for palavras in tupla:
    print(f'\nNa palavra {palavras.upper()} tem as vogais', end=' ')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
    print()
