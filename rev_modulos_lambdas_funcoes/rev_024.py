from random import randint
mat = [[randint(1, 4) for x in range(20)] for y in range(20)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(mat[l][c], end=' ')
    print()
prod1 = []
prod2 = []
prod3 = []
prod4 = []
for li in range(len(mat)):
    for co in range(len(mat)-3):
        produto1 = produto2 = produto3 = 1
        col = co
        lin = li
        c = 0
        if lin > 2:
            break
        while c < 4:
            produto1 *= mat[li][col]
            produto2 *= mat[col][li]
            produto3 *= mat[lin][col]
            col += 1
            lin += 1
            c += 1
        prod1.append(produto1)
        prod2.append(produto2)
        prod3.append(produto3)
for coluna in range(len(mat)-1, len(mat)-4, -1):
    for linha in range(len(mat)-3):
        lh = linha
        cl = coluna
        produto4 = 1
        d = 0
        while d < 4:
            produto4 *= mat[lh][cl]
            lh += 1
            cl -= 1
            d += 1
        prod4.append(produto4)
print('- ' * 15)
print('O maior produto possível nas direções:')
print(f'- Horizontal: {max(prod1)}')
print(f'- Vertical: {max(prod2)}')
print(f'- Diagonal esq para dir: {max(prod3)}')
print(f'- Diagonal dir para esq: {max(prod4)}')
