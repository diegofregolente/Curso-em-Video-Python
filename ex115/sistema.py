from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'fim_do_curso_em_video.txt'

if not arqExiste(arq):
    criarArquivo(arq)


def colors(color="neutral"):
    cores = {
        "neutral": '\033[1:30m',
        "red": '\033[1:31m',
        "green": '\033[1:32m',
        "yellow": '\033[1:33m',
        "blue": '\033[1:34m',
        "purple": '\033[1:35m',
        "cyan": '\033[1:36m',
        "grey": '\033[1:36m',
    }
    return cores[color]


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        while True:
            try:
                nome = str(input('Nome: ')).strip()
                if not nome.isalpha():
                    print(f'{colors("red")}Você não digitou uma opção válida!{colors()}')
                    continue
            except (TypeError, ValueError):
                print(f'{colors("red")}Você não digitou uma opção válida!{colors()}')
                continue
            else:
                break
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(0.5)
    elif resp == 3:
        cabecalho('Sistema finalizado... volte sempre!')
        exit()
    else:
        print(f'{colors("red")}Você não digitou uma opção válida!{colors()}')
        continue
