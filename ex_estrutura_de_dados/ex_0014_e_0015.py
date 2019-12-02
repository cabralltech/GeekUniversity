from random import randint
vet = [randint(1, 20) for num in range(10)]
print(vet)
repetidos = set()
for i in vet:
    if vet.count(i) > 1:
        repetidos.add(i)
print(repetidos)

vet1 = [randint(1, 20) for n in range(20)]
print(vet1)
repeteco = set(vet1)
print(repeteco)
