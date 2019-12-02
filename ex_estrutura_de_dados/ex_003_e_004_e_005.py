from random import randint
vet1 = [randint(1,10) for x in range(10)]
print(vet1)
vet2 = [num ** 2 for num in vet1]
print(vet2)

soma = 0
vet3 = [randint(1,9) for n in range(8)]
print(vet3)
y = int(input('Poisção y: '))
z = int(input('Posição z: '))
for i in range(len(vet3)):
    if i == z or i == y:
        soma += vet3[i]
print(f'A soma entre os valores y={y} e z={z} é {soma}')

vet4 = [randint(1,9) for m in range(10)]
evens = [e for e in vet4 if e % 2 == 0]
print(vet4)
print(evens)
print(f'A quantidade de valores pares no vetor é {len(evens)}')
