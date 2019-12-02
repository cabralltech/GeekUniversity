from random import randint
mat = [[None for x in range(5)] for y in range(5)]
for l in range(len(mat)):
    for c in range(len(mat)):
        n = randint(0, 99)
        if n not in mat:
            mat[l][c] = n
        print(f'{mat[l][c]:^5}', end='')
    print()
