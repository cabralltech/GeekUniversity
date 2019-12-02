from random import randint


def soma_trisu(m):
    soma = 0
    for li in range(len(m)):
        for co in range(len(m)):
            if li < co:
                soma += mat[li][co]
    return f'A soma dos elementos acima da diagonal principal é {soma}'


mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print('- ' * 15)
print(soma_trisu(mat))
