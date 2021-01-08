n = int(input('Digite um número: '))
print('-*'*3,'BASE DE CONVERSÃO','*-'*3)
resposta = str(input('1- Para Binário\n2- Para Octal\n3- Para Hexadecimal\n'))
if resposta == '1':
    print(bin(n)[2:])
elif resposta == '2':
    print(oct(n)[2:])
elif resposta == '3':
    print(hex(n)[2:].upper())
