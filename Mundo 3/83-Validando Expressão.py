parenE = []
parenD = []
expressao = str(input('Digite uma expressao: '))
for pos, d in enumerate(expressao):
    if d == '(':
        parenE.append('(')
    if d == ')':
        parenD.append(')')
if len(parenE) != len(parenD):
    print('Não é possível fazer uma expressão.')
else:
    print('É possível fazer uma expressão.')
