from time import sleep

def contagem(i, f, p):
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if p < 0:
        p = -p
    if i > f:
        p = -p
        f -= 1
    else:
        f += 1

    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.1)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
