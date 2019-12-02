def fat(n):
    f = 1
    for i in range(1, n+1):
        f*= i
    return f


def neperiano(n):
    nepe = sum(map(lambda x: 1 / fat(x), range(n+1)))
    return f'O resultado é {round(nepe, 2)}'



while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(neperiano(num))
