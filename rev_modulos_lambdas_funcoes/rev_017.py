from random import randint
mat = [[randint(4, 9) for x in range(3)] for y in range(10)]
for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
pior_1 = min(map(lambda a: a[0], mat))
al_min_1 = len(list(filter(lambda b: b[0] == pior_1, mat)))
print(f'A quantidade de alunxs com nota {pior_1:.1f} na primeira prova é {al_min_1}')
pior_2 = min(map(lambda d: d[1], mat))
al_min_2 = len(list(filter(lambda f: f[1] == pior_2, mat)))
print(f'A quantidade de alunxs com nota {pior_2:.1f} na segunda prova é {al_min_2}')
pior_3 = min(map(lambda g: g[2], mat))
al_min_3 = len(list(filter(lambda h: h[2] == pior_3, mat)))
print(f'A quantidade de alunxs com nota {pior_3:.1f} na terceira prova é {al_min_3}')
