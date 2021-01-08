from ex107 import moeda

n = float(input('Digite um valor: '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {n} é {moeda.aumentar(n, 10)}')
print(f'Diminuir 13% de {n} é {moeda.reduzir(n, 13)}')
