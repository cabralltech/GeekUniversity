from random import randint


def par_impar(v):
    par = [x for x in v if x % 2 == 0]
    impar = [y for y in v if y % 2 != 0]
    return f'{par}\n{"- " * 15}\n{impar}'


vetor = [randint(1, 99) for a in range(30)]
print(par_impar(vetor))
