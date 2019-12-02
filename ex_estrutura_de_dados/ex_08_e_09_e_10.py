from random import randint
soma = abaixo = igual = 0
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(3):
    for c in range(3):
        print(mat[l][c], end=' ')
        if c > l:
            soma += mat[l][c]
        elif c < l:
            abaixo += mat[l][c]
        else:
            igual += mat[l][c]

    print()
print('- ' * 10)
print(f'A soma dos elementos acima da diagonal principal é {soma}')
print(f'A soma dos elementos abaixo da diagonal principal é {abaixo}')
print(f'A soma dos elementos da diagona principal é {igual}')
