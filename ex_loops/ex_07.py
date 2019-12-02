c = soma = media = 0
while c < 10:
    num = int(input('Valor: '))
    if num > 0:
        c += 1
        soma += num
media = soma / c
print(f'A média dos números positivos digitados é {media:.1f}')
