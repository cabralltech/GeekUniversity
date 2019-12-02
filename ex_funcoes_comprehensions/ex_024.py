def piramide(num):
    n = 1
    c = num
    for x in range(1, num+1):
        c -= 1
        for y in range(c, -1, -1):
            print(' ', end='')
        print('*' * n)
        n += 2


# Programa Principal
linhas = int(input('Número de linhas: '))
piramide(linhas)
