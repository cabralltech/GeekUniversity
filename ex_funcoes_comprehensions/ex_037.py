def hiper_fat(n):
    f = x = 1
    for i in range(1, n+1):
        x = i ** i
        f *= x
    return f'O hiperfatorial de {n} é {f}'


# Programa Principal
num = int(input('Valor: '))
print(hiper_fat(num))
