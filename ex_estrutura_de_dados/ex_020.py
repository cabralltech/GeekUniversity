mat = [[0 for x in range(6)] for y in range(3)]
soma = somapar = media = cont = 0
print('- ' * 15)
for l in range(3):
    for c in range(6):
        mat[l][c] = float(input(f'[{l},{c}]: '))
        if c % 2 == 0:
            soma += mat[l][c]
        elif c == 1 or c == 3:
            somapar += mat[l][c]
            cont += 1
print('- '* 15)
for l in range(3):
    for c in range(6):
        print(f'{mat[l][c]:^5}', end="")
    print()
for l in range(3):
    mat[l][5] = mat[l][0] + mat[l][1]
print('- ' * 15)
print(f'A soma de todos os elementos das colunas ímpares é {soma}')
media = somapar / cont
print(f'A média aritmética dos elementos da 2ª e 4ª coluna é {media:.1f}')
print('- ' * 5)
for l in range(3):
    for c in range(6):
        print(f'{mat[l][c]:^5.1f}', end="")
    print()