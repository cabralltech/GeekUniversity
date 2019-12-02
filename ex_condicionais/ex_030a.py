num = []
while True:
    n = int(input('Valor: '))
    num.append(n)
    for i in range(1, len(num)):
        chave = num[i]
        k = i
        while k > 0 and chave < num[k-1]:
            num[k] = num[k-1]
            k -= 1
        num[k] = chave
    resp = ' '
    while resp not in 'NS':
        resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break
print(num)
