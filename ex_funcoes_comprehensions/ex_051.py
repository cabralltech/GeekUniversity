from random import randint


def soma_diasec(m):
    soma = 0
    co = len(m) - 1
    for lin in range(len(m)):
        for col in range(co, -1, -1):
            soma += mat[lin][col]
            break
        co -= 1
    return f'A soma dos elementos da diagonal secundária é {soma}'


mat = [[randint(1, 9) for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print('- ' * 15)
print(soma_diasec(mat))
