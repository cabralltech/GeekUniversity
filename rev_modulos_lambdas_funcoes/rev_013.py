from random import randint
mat = [[randint(1, 20) for x in range(4)] for y in range(4)]
mat_inf = [[mat[l][c] if c <= l else 0 for c in range(len(mat))] for l in range(len(mat))]
for li in range(len(mat)):
    for co in range(len(mat)):
        print(f'{mat[li][co]:^3}', end=' ')
    print(end='          ')
    for col in range(len(mat_inf)):
        print(f'{mat_inf[li][col]:^3}', end=' ')
    print()
