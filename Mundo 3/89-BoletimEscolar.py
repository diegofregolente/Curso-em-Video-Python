aluno = []
escola = []
media = 0
a = 0
while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    escola.append(aluno[:])
    aluno.clear()
    r = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if r in 'n':
        break
screen = ['No.','Nome','Média']
print(f'{screen[0]:<}{screen[1]:^10}{screen[2]:>10}')
print('-'*40)
for n, d in enumerate(escola):
    print(f' {n:<}  {d[0]:^10}  {d[3]:>6.2f}')
print('-'*40)

while True:
    a = int(input('Mostrar notas de qual aluno? (999 Para sair): '))
    if a == 999:
        print('FINALIZANDO')
        break

    print(f'As notas de {escola[a][0]} são {escola[a][1], escola[a][2]}')
    print('-' * 40)
