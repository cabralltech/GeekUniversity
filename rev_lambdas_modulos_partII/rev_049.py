from random import randint


def soma_trinf(m):
    soma = sum(sum(m[y][x] for x in range(len(m[y])) if x < y) for y in range(len(m)))
    return f'A soma dos elementos abaixo da diagonal principal é {soma}'


mat = [[randint(1, 9) for a in range(3)] for b in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(soma_trinf(mat))
