num = int(input('Valor: '))
soma = m = soma2 = soma3 = 0
for i in range(0, num+1):
    soma += i
print(f'O resultado de: 0 + 1 + 2 + 3 + ... + n = {soma}')
for i in range(0, 2*num):
    if i % 2 == 0:
        m = i * -1
    else:
        m = i
    soma2 += m
print(f'A soma de: 1 - 2 + 3 - 4 + ... + (2n - 1) = {soma2}')
for i in range(0, 2*num):
    if i % 2 != 0:
        soma3 += i
print(f'A soma de: 1 + 3 + 5 +... +(2n - 1) = {soma3}')
