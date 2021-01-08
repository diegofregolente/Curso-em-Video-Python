s = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1: # impar ou par
        if c % 3 == 0: # multiplos de 3
            s += c # soma dos numeros
            cont += 1 # contador de numero
print(f'Foram encontrados {cont} numeros e a soma deles é {s}.')
