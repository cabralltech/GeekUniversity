from random import randint


def maior_10(m):
    maior = []
    for i in range(len(m)):
        for x in range(len(m)):
            if m[i][x] > 10:
                maior.append(m[i][x])
    return f'A matriz acima contem {len(maior)} valores maiores que 10'


# Programa Principal
mat = [[randint(1, 20) for x in range(4)] for y in range(4)]
for l in range(4):
    for c in range(4):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print('- ' * 10)
print(maior_10(mat))
