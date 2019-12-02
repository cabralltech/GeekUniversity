def soma_fat(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    fat = str(f)
    fat_st = [int(x) for x in fat]
    return f'{num}! é {f} e a soma de seus algarismos é {sum(fat_st)}'


# Programa Principal
numero = int(input('Valor: '))
print(soma_fat(numero))
