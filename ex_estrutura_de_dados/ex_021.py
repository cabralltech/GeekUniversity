from random import randint
num = 0
mat1 = [[randint(1, 9) for x in range(2)] for y in range(2)]
mat2 = [[randint(1, 9) for s in range(2)] for t in range(2)]
print('- ' * 5)
for li in range(2):
    for cm in range(2):
        print(f'{mat1[li][cm]:^5}', end="")
    print()
print('- ' * 5)
for lh in range(2):
    for cn in range(2):
        print(f'{mat2[lh][cn]:^5}', end="")
    print()
print('- ' * 5)
mat3 = [[0 for m in range(2)] for n in range(2)]
mat4 = [[0 for e in range(2)] for f in range(2)]
opt = int(input('Escolha a operação:\n'
                '[ 1 ] Somar\n'
                '[ 2 ] Subtrair\n'
                '[ 3 ] Adicionar Constante\n'
                '[ 4 ] Imprimir as matrizes\n'
                'Digite a opção desejada: '))
print('- ' * 15)
if opt == 3:
    num = int(input('Constante: '))
for l in range(2):
    for c in range(2):
        if opt == 1:
            mat3[l][c] = mat1[l][c] + mat2[l][c]
        elif opt == 2:
            mat3[l][c] = mat1[l][c] - mat2[l][c]
        elif opt == 3:
            mat3[l][c] = num + mat1[l][c]
            mat4[l][c] = num + mat2[l][c]
if opt < 3:
    for ln in range(2):
        for co in range(2):
            print(f'{mat3[ln][co]:^5}', end="")
        print()
elif opt == 3:
    for ln in range(2):
        for co in range(2):
            print(f'{mat3[ln][co]:^5}', end="")
        print()
    print('- ' * 15)
    for lin in range(2):
        for col in range(2):
            print(f'{mat4[lin][col]:^5}', end="")
        print()
else:
    for ln in range(2):
        for co in range(2):
            print(f'{mat1[ln][co]:^5}', end="")
        print()
    print('- ' * 15)
    for lin in range(2):
        for col in range(2):
            print(f'{mat2[lin][col]:^5}', end="")
        print()
print('- ' * 15)
