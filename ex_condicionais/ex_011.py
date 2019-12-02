num = input('Valor: ')
soma = 0

if int(num) > 0:
    for i in range(0, len(num)):
        soma += int(num[i])
    print(f'A soma entre os algarismos é {soma}')
else:
    print('Número inválido')
