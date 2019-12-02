def fat_exp(n):
    f = 1
    for i in range(n-1, 0, -1):
        f *= i
    fex = n ** f
    return f'O fatorial exponencial de {n} é {fex}'


while True:
    try:
        num = int(input('Valor: '))
        if num <= 0:
            print('\033[31mERRO! Somente números positivos\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(fat_exp(num))
