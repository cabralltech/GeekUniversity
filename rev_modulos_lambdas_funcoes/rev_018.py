from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
mat2 = [sum(list(map(lambda a: a[x], mat))) for x in range(len(mat))]
print(mat2)
