from random import randint
vet = [randint(1, 99) for x in range(5)]
vet1 = [vet[n] if vet[n] % 2 == 1 else randint(1, 99) for n in range(5)]
print(vet)
print('- ' * 15)
print(vet1)
vet2 = [vet[d] if vet[d] % 2 == 0 else randint(1, 99) for d in range(5)]
print('- ' * 15)
print(vet2)
utilizados = (set(vet) & set(vet1)) | (set(vet) & set(vet2))
print('- ' * 15)
print(utilizados)
