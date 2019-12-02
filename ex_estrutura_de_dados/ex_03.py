from random import randint
matriz = [[randint(1, 9) for x in range(4)] for y in range(4)]
for l in range(4):
    for c in range(4):
        print(matriz[l][c], end=' ')
    print()
prod_lin = 1
prods_lin = []
for l in range(4):
    for c in range(4):
        prod_lin *= matriz[l][c]
    prods_lin.append(prod_lin)
    prod_lin = 1
print(f'Os produtos de cada linha são:')
for i in range(len(prods_lin)):
    print(f'linha {i}: {prods_lin[i]}')
prod_col = 1
prods_col = []
for c in range(4):
    for l in range(4):
        prod_col *= matriz[l][c]
    prods_col.append(prod_col)
    prod_col = 1
print(f'Os produtos de cada coluna são:')
for i in range(len(prods_col)):
    print(f'coluna {i}: {prods_col[i]}')
