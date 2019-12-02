def trian(num):
    cres = ['*' * x for x in range(1, num+1)]
    desc = ['*' * y for y in range(num-1, 0, -1)]
    for i in cres:
        print(i)
    for z in desc:
        print(z)



# Programa Principal
linhas = int(input('Número de linhas: '))
trian(linhas)
