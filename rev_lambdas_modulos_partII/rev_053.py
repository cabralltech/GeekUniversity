from random import randint


def mat_id(m):
    ident = False
    id = [[1 if a == b else 0 for a in range(len(m))]for b in range(len(m))]
    if m == id:
        ident = True
    return ident


while True:
    try:
        num = int(input('Ordem da matriz: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
mat = [[randint(0, 1) for x in range(num)] for y in range(num)]
for li in range(len(mat)):
    for co in range(len(mat)):
        print(mat[li][co], end=' ')
    print()
print(mat_id(mat))
