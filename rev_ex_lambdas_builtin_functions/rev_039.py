n = int(input('Linhas: '))
vet = [[] for b in range(n)]
for i in range(len(vet)):
    vet[i].append(1)
    if i > 1:
        v = 1
        for c in range(i-1):
            vet[i].append(vet[i-1][c] + vet[i-1][v])
            v += 1
            if v == i:
                break
    if i > 0:
        vet[i].append(1)
for x in vet:
    for y in x:
        print(y, end=' ')
    print()
