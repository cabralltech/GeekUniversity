num = []
c = 0
while c < 5:
    n = int(input('Valor: '))
    num.append(n)
    for i in range(1, len(num)):
        aux = num[i]
        k = i
        while k > 0 and aux < num[k-1]:
            num[k] = num[k-1]
            k -= 1
        num[k] = aux
    c +=1
print(num)