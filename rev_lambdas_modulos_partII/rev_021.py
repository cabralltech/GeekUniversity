def prim(z):
    prime = True
    if len([x for x in range(2, z) if z % x == 0]):
        prime = False
    return prime


def primos(n):
    prims = [y for y in range(2, n) if prim(y)]
    return prims


def n_pri(n):
    return f'A quantidade de primos abaixo de {n} é {len(primos(n))}'


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(n_pri(num))
print('- ' * 15)
print(primos(num))
