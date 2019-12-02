from random import randint


def soma_diags(m):
    so_diag = so_sec = 0
    for li in range(len(m)):
        for co in range(len(m)):
            if li == co:
                so_diag += m[li][co]
    coluna = len(m)
    for lin in range(len(m)):
        coluna -= 1
        for col in range(coluna, -1, -1):
            so_sec += m[lin][col]
            break
    soma = so_diag + so_sec
    return f'A soma dos elementos da diagonal principal e secundária é {soma}'


# Programa Principal
mat = [[randint(1, 9) for x in range(3)]for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 10)
print(soma_diags(mat))
