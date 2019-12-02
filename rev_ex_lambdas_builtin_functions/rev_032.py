from random import randint
vet1 = []
vet2 = []
c = 0
while c < 5:
    n = randint(1, 19)
    x = randint(1, 19)
    if n not in vet1 and x not in vet2:
        vet1.append(n)
        vet2.append(x)
        c += 1
print(vet1)
print('- ' * 15)
print(vet2)
print('- ' * 15)
soma = [vet1[a] + vet2[a] for a in range(len(vet1))]
print('A soma dos elementos dos vetores acima')
print(soma)
print('- ' * 15)
mult = [vet1[b] * vet2[b] for b in range(len(vet1))]
print('A multiplicação dos elementos dos vetores acima')
print(mult)
print('- ' * 15)
set1 = set(vet1) ^ set(vet2)
print(set1)
print('- ' * 15)
print(set(vet1) & set(vet2))
print('- ' * 15)
print(set(vet1) | set(vet2))

