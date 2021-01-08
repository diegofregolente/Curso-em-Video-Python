def metade(n, f=False):
    resp = n / 2
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def dobro(n, f=False):
    resp = n * 2
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def aumentar(n, a, f=False):
    resp = n + ((n * a) / 100)
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def reduzir(n, a, f=False):
    resp = n - ((n * a) / 100)
    if f:
        return f'R${resp:.2f}'.replace('.', ',')
    else:
        return resp

def real(n, moeda='R$', f=False):
    resp = n
    if f:
        return f'{moeda}{resp:.2f}'.replace('.', ',')
    else:
        return resp