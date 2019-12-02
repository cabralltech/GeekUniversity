from random import randint


def soma_col(m, c):
    soma = sum(m[x][c] for x in range(len(m)))
    return f'A soma dos elementos da coluna {c} é {soma}'


mat = [[randint(1, 9) for a in range(6)] for b in range(7)]
for lin in range(len(mat)):
    for col in range(len(mat[lin])):
        print(mat[lin][col], end=' ')
    print()
print('- ' * 15)
while True:
    try:
        coluna = int(input('Escolha uma coluna da matriz acima: '))
        if 0 <= coluna <= 6:
            break
        else:
            print('Favor digitar um número entre 0 e 6')
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print('- ' * 15)
print(soma_col(mat, coluna))
