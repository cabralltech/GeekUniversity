from random import randint


def soma_trisup(m):
    soma = sum(sum(m[y][x] for x in range(len(m[y])) if y < x) for y in range(len(m)))
    print(soma)
    return f'A soma dos elementos acima da diagonal principal é {soma}'


mat = [[randint(1, 9) for a in range(3)] for b in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(soma_trisup(mat))
