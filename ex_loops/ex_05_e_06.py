soma = 0
for i in range(1, 11):
    num = int(input(f'{i}º Valor: '))
    soma += num
print(f'A soma dos valores digitados é {soma}')

media = soma = count = 0
for i in range(1, 11):
    num = int(input(f'{i}º Valor: '))
    soma += num
    count += 1
media = soma / count
print(f'A média dos números digitados é {media:.1f}')
