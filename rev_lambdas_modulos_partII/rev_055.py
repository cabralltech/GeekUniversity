from random import randint


def somapr_sec(m):
    soprin = sum(sum(m[y][x] for x in range(len(m)) if x == y) for y in range(len(m)))
    sosec = 0
    co = len([d for d in m]) -1
    for l in range(len(m)):
        for c in range(len(m[l])):
            sosec += m[l][co]
            co -= 1
            break
    return f'A soma dos elementos da diagonal principal e secundária é {sosec + soprin}'


mat = [[randint(1, 9) for a in range(3)] for b in range(3)]
for lin in range(len(mat)):
    for col in range(len(mat[lin])):
        print(mat[lin][col], end=' ')
    print()
print('- ' * 15)
print(somapr_sec(mat))
