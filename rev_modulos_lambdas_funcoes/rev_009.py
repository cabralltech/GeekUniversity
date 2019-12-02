from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
soma = sum([sum([mat[li][co] for co in range(len(mat)) if co < li]) for li in range(len(mat))])
# for lin in range(len(mat)):
#    for col in range(len(mat)):
#        if col < lin:
#            soma += mat[lin][col]
print(f'A soma dos elementos do triânguloo inferior da matriz é {soma}')
