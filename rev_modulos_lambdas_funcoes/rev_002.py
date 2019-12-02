mat = [[1 if x == y else 0 for x in range(5)] for y in range(5)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
