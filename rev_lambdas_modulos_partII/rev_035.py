def fat_quad(n):
    f = fn = 1
    for i in range(1, n+1):
        f *= i
    for x in range(1, (2*n)+1):
        fn *= x
    fatq = fn / f
    return f'O fatorial quádruplo de {n} é {round(fatq, 2)}'


while True:
    try:
        num = int(input('Valor: '))
        if num < 0:
            print('\033[31mERRO! Somente números positivos\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(fat_quad(num))
