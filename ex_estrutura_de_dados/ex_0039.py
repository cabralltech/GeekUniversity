lis = []
lis_aux = []
v = 0
n = int(input('Número de linhas: '))
num = [[]for x in range(n)]
for i in range(n):
    if i == 0:
        num[i].append(1)
    else:
        for x in range(i):
            if x == 0:
                v = 1
            else:
                v = lis_aux[x-1] + lis_aux[x]
            lis.append(v)
        lis_aux.clear()
        for c in lis:
            num[i].append(c)
            lis_aux.append(c)
        num[i].append(1)
        lis_aux.append(1)
    lis.clear()
for a in num:
    for b in a:
        print(b, end=' ')
    print()
