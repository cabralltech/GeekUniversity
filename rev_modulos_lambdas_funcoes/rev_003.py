mat = [[x * y for x in range(4)] for y in range(4)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
