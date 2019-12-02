from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
# mat2 = [[mat[co][li] for co in range(len(mat))] for li in range(len(mat))]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print(end='          ')
    for co in range(len(mat)):
        print(mat[co][l], end=' ')
    print()
