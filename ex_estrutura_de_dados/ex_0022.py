from random import randint
vet1 = [randint(1, 9) for x in range(10)]
vet2 = [randint(1, 9) for y in range(10)]
print(vet1)
print('- ' * 10)
print(vet2)
vet3 = [vet1[z] if z % 2 == 0 else vet2[z] for z in range(10)]
print('- ' * 10)
print(vet3)
