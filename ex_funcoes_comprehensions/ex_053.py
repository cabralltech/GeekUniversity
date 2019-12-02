from random import randint


def mat_id(m):
    diag = []
    rest = []
    id = True
    for l in range(len(m)):
        for c in range(len(m)):
            if l == c:
                diag.append(m[l][c])
            else:
                rest.append(m[l][c])
    if 0 in diag:
        id = False
    elif 1 in rest:
        id = False
    if id:
        return f'A matriz gerada é uma matriz identidade'
    return f'A matriz gerada não é uma matriz identidade'


# Programa Principal
n = int(input('Ordem da matriz quadrada: '))
# mat = [[1 if x == y else 0 for x in range(n)]for y in range(n)] matriz identidade para teste
mat = [[randint(0,1) for x in range(n)]for y in range(n)]
print('- ' * 15)
for lin in range(len(mat)):
    for col in range(len(mat)):
        print(mat[lin][col], end=' ')
    print()
print('- ' * 15)
print(mat_id(mat))
