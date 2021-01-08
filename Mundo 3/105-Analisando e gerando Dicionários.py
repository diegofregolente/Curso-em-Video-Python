def notas(*n, sit=False):
    """
    -> Função média alunos
    :param n: notas dos alunos
    :param sit: situação da escola
    :return: Vamos retornar o dicionario 'escola" para a variavel retorno.
    """
    escola = {}
    escola['total'] = len(n)
    escola['maior'] = max(n)
    escola['menor'] = min(n)
    escola['média'] = sum(n) / len(n)
    if sit:
        if escola['média'] > 6:
            escola['situacao'] = 'BOA'
        else:
            escola['situacao'] = 'RUIM'
    return escola


retorno = notas(5.5, 9.5, 10, 6.5, sit=True)

print(retorno)
