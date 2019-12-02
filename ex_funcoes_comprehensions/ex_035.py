def fat_quad(num):
    f = f2 = 1
    for i in range(1, num+1):
        f *= i
    for c in range(1, 2*num+1):
        f2 *= c
    fat = f2 / f
    return f'O fatorial quádruplo de {num} é {fat}'


# Programa Principal
numero = int(input('Valor: '))
print(fat_quad(numero))
