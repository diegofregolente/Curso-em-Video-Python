from ex108 import moeda

n = float(input('Digite um valor: '))
print(f'A metade de {moeda.real(n)} é {moeda.metade(n)}')
print(f'O dobro de {moeda.real(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {moeda.real(n)} é {moeda.aumentar(n, 10)}')
print(f'Diminuir 13% de {moeda.real(n)} é {moeda.reduzir(n, 13)}')
