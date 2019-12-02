from random import randint
mat = [[randint(1, 20) if x <= y else 0 for x in range(4)] for y in range(4)]
for l in range(4):
    for c in range(4):
        if mat[l][c] != 0:
            print(f'{mat[l][c]:^5}', end=' ')
    print()
