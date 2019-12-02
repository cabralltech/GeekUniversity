from random import randint


def mult_mat(ma, mb):
    mc = [[0 for x in range(len(mb[y]))] for y in range(len(mb))]
    for l in range(len(ma)):
        for c in range(len(ma[l])):
            soma = 0
            co = 0
            while co < len(ma[l]):
                soma += ma[l][co] * mb[co][c]
                co += 1
            mc[l][c] = soma
    for lin in range(len(mc)):
        for col in range(len(mc[lin])):
            print(f'{mc[lin][col]:^5}', end=' ')
        print()


while True:
    try:
        ordem = int(input('Ordem das matrizes: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
mat1 = [[randint(1, 5) for a in range(ordem)] for b in range(ordem)]
mat2 = [[randint(1, 5) for k in range(ordem)] for j in range(ordem)]
for linha in range(len(mat1)):
    for coluna in range(len(mat1[linha])):
        print(mat1[linha][coluna], end=' ')
    print(end=' ' * 10)
    for colun in range(len(mat2[linha])):
        print(mat2[linha][colun], end=' ')
    print()
print('- ' * 15)
mult_mat(mat1, mat2)
