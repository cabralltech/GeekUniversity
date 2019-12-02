from random import randint


def soma_linha(m, n):
    """
    Sums up the elements of a given line as argument
    :param m: matrix generated
    :param n: line for sum of elements
    :return: The sum of the pointed line
    """
    soma = 0
    for co in range(len(m[n])):
        soma += m[n][co]
    return f'A soma dos elementos da linha {n} é {soma}'


mat = [[randint(1, 9) for x in range(6)] for y in range(7)]
for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
while True:
    linha = int(input('Escolha uma linha para a soma de seus elementos: '))
    if 0 <= linha <= 6:
        break
    else:
        print('\033[31mERRO! Digite um número de 0 a 6.\n')
print('- ' * 15)
print(soma_linha(mat, linha))
