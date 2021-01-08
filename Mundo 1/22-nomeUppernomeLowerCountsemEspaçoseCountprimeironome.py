nome = str(input('Digite seu nome completo: ')).strip().lower()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) # pode ser usado o nome.replace(' ','') também.
dividido = nome.split()
print(len(dividido[0]))
