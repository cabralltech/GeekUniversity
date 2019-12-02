c = 0
n = int(input('Número de linhas: '))
for l in range(1, n+1):
    for x in range(1, l+1):
        c += 1
        print(c, end=' ')
    print()