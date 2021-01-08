preco = float(input('Digite o valor do produto R$: '))
condicao = str(input('''Qual a condição de pagamento?
1 - Á vista no dinheiro/cheque 10% de desconto
2 - Á vista no cartão 5% de desconto
3 - 2x no cartão preço normal
4 - 3x ou mais no cartão 20% de juros
'''))
if condicao == '1':
    desconto = preco - (preco * (10/100))
    print(f'O valor da compra vai sair a {desconto:.2f} R$.')
elif condicao == '2':
    desconto = preco - (preco * (5/100))
    print(f'O valor da compra vai sair a {desconto:.2f} R$.')
elif condicao == '3':
    parcela = preco / 2
    print(f'O valor da compra vai ser {preco} e a parcela vai ser de {parcela} R$ em 2 vezes.')
elif condicao == '4':
    qntParcela = int(input('Vai ser em quantas vezes? '))
    juros = preco + (preco * (20/100))
    parcela = juros / qntParcela
    print(f'Nessa condicao o valor com 20% de juros vai sair {juros} e a parcela vai ser {qntParcela} vezes de {parcela} R$')
