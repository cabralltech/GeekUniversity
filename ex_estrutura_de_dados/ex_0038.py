num = []
for i in range(10):
    n = int(input('Valor: '))
    num.append(n)
    for c in range(1, len(num)):
        aux = num[c]
        d = c
        while d > 0 and aux <= num[d-1]:
            num[d] = num[d-1]
            d -= 1
        num[d] = aux
print(num)
