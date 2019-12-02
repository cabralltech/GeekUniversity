mat = [[None for x in range(10)] for y in range(10)]
for l in range(10):
    for c in range(10):
        if l < c:
            mat[l][c] = (2 * l) + (7 * c)
        elif l > c:
            mat[l][c] = (4 * (l ** 3)) - (5 * (c ** 2)) + 1
        else:
            mat[l][c] = (3 * (l ** 2)) - 1
        print(f'[{mat[l][c]:^7}]', end=' ')
    print()