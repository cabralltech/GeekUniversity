from random import randint


def par_impar(n):
    evens = [x for x in n if x % 2 == 0 and x != 0]
    odds = [y for y in n if y % 2 != 0]
    return f'Números pares: {evens}\nNúmeros ímpares: {odds}'


# Programa Principal
num = [randint(1, 100) for a in range(30)]
print(par_impar(num))
