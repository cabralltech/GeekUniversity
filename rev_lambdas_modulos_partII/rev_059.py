from random import randint


def uniao(v1, v2):
    return set(v1) | set(v2)


vet1 = [randint(1, 20) for x in range(10)]
print(vet1)
print('- ' * 5)
vet2 = [randint(1, 20) for y in range(10)]
print(vet2)
print('- ' * 15)
print(uniao(vet1, vet2))
