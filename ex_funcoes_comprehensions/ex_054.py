from random import randint


def soma_mat(m):
    soma = 0
    for l in range(len(m)):
        for c in range(len(m)):
            soma += m[l][c]
    return f'A soma dos elementos da matriz gerada é {soma}'


# Programa Principal
mat = [[randint(1, 9) for x in range(4)]for y in range(4)]
for li in range(len(mat)):
    for co in range(len(mat)):
        print(f'[{mat[li][co]:^5}]', end='')
    print()
print('- ' * 5)
print(soma_mat(mat))
