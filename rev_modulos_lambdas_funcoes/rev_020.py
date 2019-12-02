from random import uniform
mat = [[round(uniform(0, 9), 1) for x in range(6)] for y in range(3)]
print('Matriz original: ')
for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(f'{mat[l][c]:^5}', end=' ')
    print()
print('- ' * 15)
soma_impares = sum([sum([mat[li][co] for co in range(
    len(mat[li])) if co % 2 == 0]) for li in range(len(mat))])
print(f'A soma dos elementos das colunas ímpares é {round(soma_impares, 1)}')
med_col_1 = sum([sum(map(lambda a: a[k], mat))
                 for k in range(len(mat[0])) if k == 1]) / len(mat)
med_col_2 = sum([sum(map(lambda b: b[p], mat))
                 for p in range(len(mat[0])) if p == 3]) / len(mat)
print(f'A média arit. da 2ª coluna é {round(med_col_1, 1)}')
print(f'A média arit. da 4ª coluna é  {round(med_col_2, 1)}')
mat2 = [[round(mat[lin][0] + mat[lin][1], 1) if col == 5 else mat[lin][col]
         for col in range(len(mat[lin]))] for lin in range(len(mat))]
print('- ' * 15)
print('Matriz modificada:')
for linha in range(len(mat2)):
    for coluna in range(len(mat2[linha])):
        print(f'{mat2[linha][coluna]:^5}', end=' ')
    print()
