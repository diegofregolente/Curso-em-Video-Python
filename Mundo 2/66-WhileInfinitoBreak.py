n = 0
c = 0
s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} e a soma foi {s}')