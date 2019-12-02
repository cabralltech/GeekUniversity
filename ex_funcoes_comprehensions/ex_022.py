def exclamacao(num):
    excl = ['!' * x for x in range(1, num+1)]
    for i in excl:
        print(i)


# Programa Principal
linhas = int(input('Número de linhas: '))
exclamacao(linhas)

