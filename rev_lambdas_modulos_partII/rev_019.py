def primo(z):
    prime = True
    if len(list(
        filter(lambda x: z % x == 0, range(2, z))
    )):
        prime = False
    return prime


def primos(n):
    prims = [x for x in range(2, n) if primo(x)]
    return prims


def maior_fatoral(n):
    pri = primos(n)
    fatoral = list(filter(lambda a: n % a == 0, pri))
    return f'O maior fatoral de {n} é {max(fatoral)}'


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(maior_fatoral(num))
