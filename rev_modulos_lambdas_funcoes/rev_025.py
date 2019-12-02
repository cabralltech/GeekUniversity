from random import randint
mat = [[0 for x in range(3)] for y in range(3)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'{mat[l][c]:^5}', end=' ')
    print()
print('- ' * 25)
while True:
    while True:
        li_com = randint(0, 2)
        co_com = randint(0, 2)
        if mat[li_com][co_com] == 0:
            mat[li_com][co_com] = 1
            break
    for li in range(len(mat)):
        for co in range(len(mat)):
            print(f'{mat[li][co]:^5}', end=' ')
        print()
    while True:
        while True:
            try:
                linha = int(input('Digite um valor para linha (de 0 a 2): '))
                if 0 <= linha <= 2:
                    break
                else:
                    print('\033[31mERRO! Somente números de 0 a 2\033[m')
            except ValueError:
                print('\033[31mERRO! Somente números de 0 a 2\033[m')
        print('- ' * 5)
        while True:
            try:
                coluna = int(input('Digite um valor para coluna (de 0 a 2): '))
                if 0 <= coluna <= 2:
                    break
                else:
                    print('\033[31mERRO! Somente números de 0 a 2\033[m')
            except ValueError:
                print('\033[31mERRO! Somente números de 0 a 2\033[m')
        if mat[linha][coluna] == 0:
            mat[linha][coluna] = -1
            break
    for li in range(len(mat)):
        for co in range(len(mat)):
            print(f'{mat[li][co]:^5}', end=' ')
        print()
    res = input('Continuar? ').strip().upper()[0]
    if res == 'N':
        break
    print('- ' * 15)
print('- ' * 25)
print('JOGO ENCERRADO')
