from random import randint


def transposta(m):
    trans = [[m[x][y] for x in range(len(m[y]))] for y in range(len(m))]
    for l in range(len(trans)):
        for c in range(len(trans)):
            print(trans[l][c], end=' ')
        print()


while True:
    try:
        n = int(input('Ordem da matriz: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
mat = [[randint(1, 9) for a in range(n)] for b in range(n)]
for li in range(len(mat)):
    for co in range(len(mat)):
        print(mat[li][co], end=' ')
    print()
print('- ' * 15)
transposta(mat)
