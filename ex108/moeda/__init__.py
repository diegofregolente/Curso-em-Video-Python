def metade(n):
    resp = n / 2
    return f'R${resp:.2f}'.replace('.',',')

def dobro(n):
    resp = n * 2
    return f'R${resp:.2f}'.replace('.',',')

def aumentar(n, a):
    resp = n + ((n * a) / 100)
    return f'R${resp:.2f}'.replace('.',',')

def reduzir(n, a):
    resp = n - ((n * a) / 100)
    return f'R${resp:.2f}'.replace('.',',')

def real(n, moeda='R$'):
    resp = n
    return f'{moeda}{resp:.2f}'.replace('.',',')