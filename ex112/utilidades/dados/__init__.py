def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0:31mERRO, é um preço invalido.\033[m')
        else:
            válido = True
            return float(entrada)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[0:31mValor inserido não é um numero inteiro\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0:31mPrograma encerrado por usuário.\033[m')
            return 0
        except Exception as erro:
            print(f'\033[0:31mNão foi possível inserir o valor por causa do {erro.__class__}\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[0:31mValor inserido não é um numero real\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0:31mPrograma encerrado por usuário.\033[m')
            return 0
        except Exception as erro:
            print(f'\033[0:31mNão foi possível inserir o valor por causa do {erro.__class__}\033[m')
            continue
        else:
            return n
