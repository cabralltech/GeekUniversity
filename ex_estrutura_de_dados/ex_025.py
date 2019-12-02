from random import randint
mat = [['-' for x in range(3)] for y in range(3)]
print('= ' * 10)
jogador = computador = ' '
while jogador not in 'XO':
    jogador = input('Escolha "X" ou "O": ').strip().upper()[0]
if jogador == 'X':
    computador = 'O'
elif jogador == 'O':
    computador = 'X'
for l in range(3):
    for c in range(3):
        print(mat[l][c], end=' ')
    print()
while True:
    print('= ' * 10)
    lin = int(input('Linha: '))
    col = int(input('Coluna: '))
    print('= ' * 10)
    while True:
        linha = randint(0, 2)
        coluna = randint(0,2)
        if mat[linha][coluna] == '-':
            break
    for ln in range(3):
        for co in range(3):
            if ln == linha and co == coluna:
                mat[ln][co] = computador
            elif ln == lin and co == col:
                mat[ln][co] = jogador
            print(mat[ln][co], end=' ')
        print()
    print('= ' * 10)
    resp = ' '
    while resp not in 'NS':
        resp = input('Mais uma jogada? ').strip().upper()[0]
    if resp == 'N':
        break
