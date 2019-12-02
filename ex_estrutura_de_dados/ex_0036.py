num = []
for i in range(10):
    n = float(input('Valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
    else:
        p = 0
        while p < len(num):
            if n <= num[p]:
                num.insert(p, n)
                break
            p += 1
for c in num:
    print(c, end=' ')
