num = int(input('Número de termos: '))
fat = []
for i in range(2, 2*num+1, 2):
    f = 1
    for c in range(1, i+1):
        f *= c
    fat.append(f)
print(fat)
som = [1 / fat[x] for x in range(num)]
print(som)
soma = 0
for y in som:
    soma += y
print(soma)

