def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional) Mostra ou não na tela
    :return: o Valor do Fatorial de um número n
    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print('-' * 20)
print(fatorial(5, show=True))
