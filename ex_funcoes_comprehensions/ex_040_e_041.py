from random import randint


def conta_pares(n):
    pares = [x for x in n if x % 2 == 0 and x != 0]
    return f'{n}\n{"- " * 5}\nExistem {len(pares)} números pares na lista acima'


def maior(n):
    ma = 0
    for i in range(len(n)):
        if i == 0:
            ma = n[i]
        else:
            if n[i] > ma:
                ma = n[i]
    return f'O maior número da lista é {ma}'


num = [randint(1, 50) for y in range(10)]
print(conta_pares(num))
print('- ' * 10)
print(maior(num))
