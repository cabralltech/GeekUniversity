def superfat(n):
    sf = 1
    for i in range(1, n+1):
        f = 1
        for c in range(1, i+1):
            f *= c
        sf *= f
    return f'O super fatorial de {n} é {sf}'


while True:
    try:
        num = int(input('Valor: '))
        if num <= 0:
            print('\033[31mERRO! Somente valores positivos\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(superfat(num))
