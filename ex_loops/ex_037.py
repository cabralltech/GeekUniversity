sep = ' '
n1 = n2 = somaquad = 0
for i in range(1000, 10000):
    sep = str(i)
    n1 = int(sep[:2])
    n2 = int(sep[2:])
    somaquad = (n1 + n2) ** 2
    if somaquad == i:
        print(i, end=' ')
