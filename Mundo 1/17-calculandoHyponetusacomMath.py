import math
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
print(f'Hipotenusa = {math.hypot(oposto, adjacente):.2f}')
