num = int(input('Digite um valor: '))
factorial = 1
while num > 1:
    factorial = num * factorial
    num -= 1
print(factorial)

for i in range(num, 1, -1):
    factorial = num * factorial
print(factorial)
