from random import randint
mat1 = [[randint(1, 9) for x in range(4)] for y in range(4)]
mat2 = [[randint(1, 9)for v in range(4)] for h in range(4)]
mat3 = [[mat1[d][r] if mat1[d][r] > mat2[d][r] else mat2[d][r] for r in range(4)] for d in range(4)]
for l in range(len(mat1)):
    for c in range(len(mat1)):
        print(mat1[l][c], end=' ')
    print(end='     ')
    for col in range(len(mat2)):
        print(mat2[l][col], end=' ')
    print(end='     ')
    for co in range(len(mat3)):
        print(mat3[l][co], end=' ')
    print()
