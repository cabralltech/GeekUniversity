mat = [[0 for x in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        if i < j:
            mat[i][j] = (2 * i) + (7 * j) - 2
        elif i == j:
            mat[i][j] = (3 * (i ** 2)) - 1
        else:
            mat[i][j] = (4 * (i ** 2)) - (5 * (j ** 2)) + 1
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'[{mat[l][c]:^5}]', end=' ')
    print()
