from random import randint


def prod_mat(m1, m2):
    m3 = [[] for y in range(len(m1))]
    for li in range(len(m3)):
        for co in range(len(m3)):
            c = 0
            soma = 0
            while c < len(m3):
                soma += m1[li][c] * m2[c][co]
                c += 1
            m3[li].append(soma)
    print(f'O produto das duas matrizes é: ')
    print('- ' * 15)
    for lin in range(len(m3)):
        for col in range(len(m3)):
            print(f'{m3[lin][col]:^5}', end=' ')
        print()


# Programa Principal
linhas = int(input('Ordem das matrizes: '))
mat_a = [[randint(0, 9) for x in range(linhas)] for y in range(linhas)]
mat_b = [[randint(0, 9) for r in range(linhas)] for f in range(linhas)]
for l in range(len(mat_a)):
    for c in range(len(mat_a)):
        print(mat_a[l][c], end=' ')
    print(end='     ')
    for m in range(len(mat_b)):
        print(mat_b[l][m], end=' ')
    print()
print('- ' * 15)
prod_mat(mat_a, mat_b)
