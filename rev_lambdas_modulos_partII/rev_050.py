from random import randint


def soma_diagpr(m):
    soma = sum(sum(m[y][x] for x in range(len(m[y])) if x == y) for y in range(len(m)))
    return f'A soma dos elementos da diagonal principal é {soma}'


mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(soma_diagpr(mat))
