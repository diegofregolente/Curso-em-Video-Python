def metade(n, f=True):
    resp = n / 2
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def dobro(n, f=True):
    resp = n * 2
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def aumentar(n, a, f=True):
    resp = n + ((n * a) / 100)
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def reduzir(n, r, f=True):
    resp = n - ((n * r) / 100)
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def real(n, moeda='R$', f=True):
    resp = n
    if f:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp

def resumo(n=0, a=10, r=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(25))
    print('-' * 30)
    print(f'Preço analisado: \t{real(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{r}% de redução: \t{reduzir(n, r)}')
    print('-' * 30)
