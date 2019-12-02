num = []
while True:
    n = int(input('Valor: '))
    num.append(n)
    for i in range(1, len(num)):
        for k in range(0, len(num)-1):
            if num[i] < num[k]:
                aux = num[i]
                num[i] = num[k]
                num[k] = aux
    resp = ' '
    while resp not in 'NS':
        resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break
print(num)
