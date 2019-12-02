from random import randint


def soma_coluna(m, n):
    """
    Sums up a column given as argument
    :param m: matrix for identifying column
    :param n: given colunm
    :return: the sum of the elements of the given column
    """
    soma = 0
    for l in range(len(m)):
        soma += m[l][n]
    return f'A soma dos elementos da coluna {n} é {soma}'


mat = [[randint(1, 9) for x in range(6)]for y in range(7)]
for lin in range(len(mat)):
    for col in range(len(mat[lin])):
        print(mat[lin][col], end=' ')
    print()
print('- ' * 15)
while True:
    coluna = int(input('Coluna a ser somada: '))
    if 0 <= coluna <= 5:
        break
    else:
        print('\033[31mERRO! Digite um núemro de 0 a 5.')
print(soma_coluna(mat, coluna))
