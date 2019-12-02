num = int(input('Valor: '))
soma = 0
c = 1
while c < num:
    if num % c == 0:
        soma += c
        print(c, end=' ')
    c += 1
print(f'\nA soma dos divisores de {num} é {soma}')