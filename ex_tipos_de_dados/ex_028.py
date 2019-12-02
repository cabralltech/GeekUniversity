soma = quad = 0
for i in range(1, 4):
    num = int(input('Valor: '))
    quad = num ** 2
    soma += quad
print(f'A soma dos quadrados dos números digitados é {soma}')
