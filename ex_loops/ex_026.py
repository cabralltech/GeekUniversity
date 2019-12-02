num = int(input('Valor: '))
c = num + 1
while True:
    if c % 11 == 0 or c % 13 == 0 or c % 17 == 0:
        break
    c += 1
print(f'O primeiro múltiplo de 11, 13 ou 17 depois de {num} é: {c}')
