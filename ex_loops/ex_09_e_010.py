n = int(input('Valor: '))
for i in range(1, ((n-1)*2)+2, 2):
    print(i, end=' ')
print()

soma = 0
for i in range(2, 101, 2):
    print(i, end=' ')
    soma += i
print(f'\nA soma dos primeiros 50 números pares é {soma}')
