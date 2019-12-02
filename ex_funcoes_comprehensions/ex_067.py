def vet(pal, x):
    x = len(pal)
    vet1 = set()

    def getchar(x):
        for i in range(x):
            i = input('Valor: ')
    vet1.add(getchar(x))
    return vet1


caracteres = {'a', 'b', 'c', 'd', 'e', 'f'}
n = len(caracteres)
print(vet(caracteres, n))
