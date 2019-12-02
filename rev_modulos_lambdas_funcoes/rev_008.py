from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
soma = 0
for lin in range(len(mat)):
    for col in range(len(mat)):
        if lin < col:
            soma += mat[lin][col]
print(f'A soma do triangulo superior da matriz é {soma}')
