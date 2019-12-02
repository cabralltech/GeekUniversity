from random import randint
mat1 = [[randint(1, 9) for x in range(3)] for y in range(3)]
mat2 = [[randint(1, 9) for a in range(3)] for b in range(3)]
for l in range(len(mat1)):
    for c in range(len(mat1)):
        print(mat1[l][c], end=' ')
    print(end=' ' * 10)
    for co in range(len(mat2)):
        print(mat2[l][co], end=' ')
    print()
print('- ' * 15)
mat3 = [[0 for yps in range(len(mat1[xis]))]for xis in range(len(mat1))]
for lin in range(len(mat1)):
    for col in range(len(mat1)):
        soma = 0
        for coluna in range(len(mat1)):
            soma += mat1[lin][coluna] * mat2[coluna][col]
        mat3[lin][col] = soma
for linha in range(len(mat3)):
    for coluna in range(len(mat3)):
        print(f'{mat3[linha][coluna]:^5}', end=' ')
    print()
