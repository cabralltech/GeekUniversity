num = int(input('Valor: '))
print(f'Os divisores de {num} são: ', end='')
for i in range(num, 0, -1):
    if num % i == 0:
        print(i, end=' ')
