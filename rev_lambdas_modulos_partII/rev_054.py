from random import randint


def soma_mat(m):
    soma = sum(sum(m[y][x] for x in range(len(m[y]))) for y in range(len(m)))
    return f'A soma dos elementos da matriz é {soma}'


mat = [[randint(1, 9) for a in range(4)] for b in range(4)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(soma_mat(mat))
