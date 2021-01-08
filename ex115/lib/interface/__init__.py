def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(f'{colors("red")}Você não digitou uma opção válida!{colors()}')
            continue
        else:
            return n


def colors(color="neutral"):
    cores = {
        "neutral":'\033[1:30m',
        "red":'\033[1:31m',
        "green":'\033[1:32m',
        "yellow":'\033[1:33m',
        "blue":'\033[1:34m',
        "purple":'\033[1:35m',
        "cyan":'\033[1:36m',
        "grey":'\033[1:36m',
    }
    return cores[color]


def linha(tam=50):
    return '-'*40


def cabecalho(txt='MENU PRINCIPAL'):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lst):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'{colors("yellow")}{c} - {colors("blue")}{item}{colors()}')
        c += 1
    opc = leiaInt(f'{colors("green")}Sua Opção: {colors()}')
    return opc