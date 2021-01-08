a = int(input('Reta A: '))
b = int(input('Reta B: '))
c = int(input('Reta C: '))
if a < b + c and b < a + c and c < a + b:
    print('Com essas medidas podemos fazer um triângulo.')
    if a == b == c:
        print('O triangulo é um equilatero')
    elif a == b or a == c or b == c:
        print('O triangulo é um isosceles')
    elif a != b and a != c and b != c:
        print('O triangulo é escaleno')
else:
    print("Não é possivel fazer um triangulo com essas medidas.")
