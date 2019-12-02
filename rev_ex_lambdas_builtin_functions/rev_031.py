from random import randint
vet1 = [randint(1, 49) for x in range(10)]
vet2 = [randint(1, 49) for y in range(10)]
print(vet1)
print('- ' * 15)
print(vet2)
print('- ' * 15)
vet = set(vet1) | set(vet2)
print(vet)
