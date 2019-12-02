from random import randint


def transposta(m):
    trans = [[m[x][y] for x in range(len(m))] for y in range(len(m))]
    return trans


n = int(input('Matriz de ordem: '))
mat = [[randint(1, 9) for x in range(n)] for y in range(n)]

for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print('- '* 15)
transp = transposta(mat)
for lin in range(len(transp)):
    for col in range(len(transp)):
        print(f'[{transp[lin][col]:^5}]', end='')
    print()