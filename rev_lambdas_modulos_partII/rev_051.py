from random import randint


def soma_diagsec(m):
    soma = 0
    col = len([d for d in range(len(m))])
    for y in range(len(m)):
        col -= 1
        for x in range(len(m[y])-1, ):
            soma += m[y][col]
            break
    return f'A soma dos elementos da diagonal secundária é {soma}'


mat = [[randint(1, 9) for a in range(3)] for b in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(soma_diagsec(mat))
