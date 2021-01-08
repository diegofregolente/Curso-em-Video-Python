nome = str(input('Qual o nome do aluno? '))
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1 + nota2) / 2
print(f'A média do {nome} foi {round(media):.2f}')
if media >= 7:
    print(f'PARABENS! {nome} é um dos aprovados!')
else:
    print(f'Oh... parece que dessa vez você foi reprovado, te vejo no exame! :(')
