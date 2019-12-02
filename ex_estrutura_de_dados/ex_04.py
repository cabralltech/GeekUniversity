from random import randint
matriz = [[randint(100, 999) for x in range(4)] for  y in range(4)]
maior = 0
for l in range(4):
    for c in range(4):
        print(matriz[l][c], end=' ')
    print()
for lin in range(4):
    for col in range(4):
        if lin == 0 == col:
            maior = matriz[lin][col]
        else:
            if matriz[lin][col] > maior:
                maior = matriz[lin][col]
print(f'O maior valor da matriz é {maior}')
