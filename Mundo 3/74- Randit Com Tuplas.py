from random import randint
n = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),)
maior = 0
menor = 0
for pos, numero in enumerate(n):
    print(numero, end=' ')
print()
print(max(n))
print(min(n))
