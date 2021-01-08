def area(larg, compr):
    r1 = larg * compr
    return r1

# CORE PROGRAM
print(' -CALCULO DE AREA- ')
print('-' * 50)
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))

r1 = area(largura, comprimento)
print(f'A área de {largura:.1f} x {comprimento:.1f} é de {r1}m².')
