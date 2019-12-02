from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
print('Matriz original: ')
for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(mat[l][c], end=' ')
    print()
mat_quad = [[0 for xis in range(len(mat[yps]))] for yps in range(len(mat))]
print('- ' * 15)
print('Matriz quadrada: ')
for li in range(len(mat)):
    for co in range(len(mat[li])):
        soma = 0
        for col in range(len(mat[co])):
            soma += mat[li][col] * mat[col][co]
        mat_quad[li][co] = soma
for linha in range(len(mat_quad)):
    for coluna in range(len(mat_quad[linha])):
        print(f'{mat_quad[linha][coluna]:^5}', end=' ')
    print()
