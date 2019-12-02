def nep(num):
    fat = []
    for i in range(1, num):
        f = 1
        for c in range(1, i+1):
            f *= c
        fat.append(f)
    print(fat)
    fat.insert(0, 1)
    neper = [1 / fat[x] for x in range(num)]
    print(neper)
    neper.insert(0, 1)
    soma = 0
    for y in neper:
        soma += y
    return f'O número neperiano até 5 é {soma:.2f}'


# Programa Principal
numero = int(input('Valor: '))
print(nep(numero))
