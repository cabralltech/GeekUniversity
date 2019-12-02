matriz = [[0 if x != y else 1 for x in range(5)] for y in range(5)]
for lin in range(5):
    for col in range(5):
        print(matriz[lin][col], end=' ')
    print()

