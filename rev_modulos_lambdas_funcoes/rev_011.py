from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
soma = 0
col = len(mat) - 1
for li in range(len(mat)):
    for co in range(1):
        soma += mat[li][col]
        break
    col -= 1
print(f'A soma dos elementos da diagonal secundária é {soma}')