from random import randint


def desvio_padrao(v):
    med = sum(v) / len(v)
    somat = sum((x-med) ** 2 for x in v)
    desvio = (somat / (len(v) - 1)) ** 0.5
    return f'{v}\n{"- " * 15}\nO desvio padrão é {round(desvio, 2)}'


vet = [randint(1, 20) for c in range(5)]
print(desvio_padrao(vet))
