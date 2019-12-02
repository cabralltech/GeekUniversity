from random import randint


def uniao_vet(v1, v2):
    v3 = v1 + v2
    return v3


# Programa Principal
vet1 = [randint(1, 9) for x in range(10)]
print(vet1)
print('- ' * 15)
vet2 = [randint(1, 9) for y in range(10)]
print(vet2)
print('- ' * 15)
print(uniao_vet(vet1, vet2))
