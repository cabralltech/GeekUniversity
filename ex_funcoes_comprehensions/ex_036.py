def super_fat(n):
    f = super = 1
    for i in range(1, n+1):
        f = 1
        for x in range(1, i+1):
            f *= x
        super *= f
    return f'O superfatorial de {n} é {super}'


# Programa Principal
num = int(input('Valor: '))
print(super_fat(num))
