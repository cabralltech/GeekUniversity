def fat_duplo(n):
    f = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            f *= i
    return f'O fatorial duplo de {n} é {f}'


while True:
    try:
        num = int(input('Valor ímpar: '))
        if num % 2 == 0:
            print('\033[31mERRO! Somente valores ímpares\033[m')
        elif num < 0:
            print('\033[31mERRO! Somente valores positivos\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print('- ' * 5)
print(fat_duplo(num))
