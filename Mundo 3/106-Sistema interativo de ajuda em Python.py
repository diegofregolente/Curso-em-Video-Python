bibli = ''

while True:
    from time import sleep

    def escreva(palavra):
        tam = len(palavra)
        print('\33[0:30:31m~'*(tam+4))
        print(f'  {palavra}')
        print('~' * (tam + 4))
        sleep(0.5)
        return palavra

    def biblioteca(funcao):
        text = f" Acessando o manual do comando  '{funcao}'"
        tam = len(text)
        print('\33[0:30:32m~' * (tam + 4))
        print(f" Acessando o manual do comando  '{funcao}'\033[0:30:34m")
        print('~' * (tam + 4))
        sleep(0.5)
        help(funcao)
        sleep(0.5)


    sistem_screen = escreva('SISTEMA DE AJUDA PyHELP')

    bibli = str(input('\033[0:30mFunção ou Biblioteca > ')).lower().strip()

    if bibli == 'fim':
        break
    else:
        biblioteca(bibli)