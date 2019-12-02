from random import randint
maior = menor = 0
vet = [randint(1, 9) for x in range(10)]
for i in range(len(vet)):
    if i == 0:
        maior = menor = vet[i]
    else:
        if vet[i] > maior:
            maior = vet[i]
        if vet[i] < menor:
            menor = vet[i]
print(vet)
print(f'O maior valor é {maior} e o menor valor é {menor}')

vet1 = [randint(1, 99) for y in range(10)]
ma = pos = 0
for c in range(len(vet1)):
    if c == 0:
        ma = vet1[c]
        pos = c
    else:
        if vet1[c] > ma:
            ma = vet1[c]
            pos = c
print(vet1)
print(f'O maior valor é {ma} e está na posição {pos}')

vet2 = [randint(1, 99) for z in range(6)]
print(vet2)
for n in range(len(vet2)-1, -1, -1):
    print(vet2[n], end=' ')
