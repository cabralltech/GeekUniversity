from random import randint

mat = [[randint(1, 9) for x in range(3)] for y in range(3)]

for l in range(3):
    for c in range(3):
        print(mat[l][c], end=' ')
    print()
print('- ' * 5)
for l in range(3):
    for c in range(3):
        print(mat[c][l], end=' ')
    print()

