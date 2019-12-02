num = []
c = 0
while True:
    n = int(input('Valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num) and n <= num[pos]:
            num.insert(pos, n)
            pos += 1
            break
    c += 1
    resp = ' '
    while resp not in 'NS':
        resp = input('Quer cadastrar outro número? ').strip().upper()[0]
    if resp == 'N':
        break
print(num)
