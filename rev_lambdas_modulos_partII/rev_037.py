def hiper_fat(n):
    hf = 1
    for i in range(1, n+1):
        hf *= i ** i
    return f'O hiperfatorial de {n} é {hf}'


while True:
    try:
        num = int(input('Valor: '))
        if num <= 0:
            print('\033[31mERRO! Somente valores positivos\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(hiper_fat(num))
