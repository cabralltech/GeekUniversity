from random import randint
mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(3):
    for c in range(3):
        print(mat[l][c], end=' ')
    print()

print('- ' * 10)
lin = soma = 0
col = len(mat) - 1

while col >= 0:
    soma += mat[lin][col]
    lin += 1
    col -= 1
print(f'A soma dos elementos da diagonal secundária é {soma}')
