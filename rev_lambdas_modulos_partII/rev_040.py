from random import randint


def pares(v):
    par = len([x for x in v if x % 2 == 0])
    return f'{v}\n{"- " * 15}\nA quantidade de números pares é {par}'


n = randint(5, 20)
vet = [randint(10, 100) for y in range(n+1)]
print(pares(vet))
