def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return print(f'Com {idade} seu voto é NEGADO')
    elif 18 <= idade < 65:
        return print(f'Com {idade} seu voto é OBRIGATÓRIO')
    else:
        return print(f'Com {idade} seu voto é OPCIONAL')


anoNasc = int(input('Digite seu ano de nascimento? '))
voto(anoNasc)
