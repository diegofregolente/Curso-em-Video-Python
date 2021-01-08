nome = str(input('Digite um nome completo: ')).strip().title()
nomeseparado = nome.split()
print(f'Primeiro nome:', nomeseparado[0])
print(f'Ultimo nome:', nomeseparado[-1])