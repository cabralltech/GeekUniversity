from random import randint
mat1 = [[randint(1, 9) for x in range(4)] for y in range(4)]
mat2 = [[randint(1, 9) for a in range(4)] for b in range(4)]
mat3 = [[None for s in range(4)] for t in range(4)]
for lin in range(4):
    for col in range(4):
        if mat1[lin][col] > mat2[lin][col]:
            mat3[lin][col] = mat1[lin][col]
        else:
            mat3[lin][col] = mat2[lin][col]
print('- '* 5)
for l in range(4):
    for c in range(4):
        print(mat1[l][c], end=' ')
    print()
print('- ' * 5)
for ln in range(4):
    for co in range(4):
        print(mat2[ln][co], end=' ')
    print()
print('- ' * 5)
for li in range(4):
    for cm in range(4):
        print(mat3[li][cm], end=' ')
    print()
