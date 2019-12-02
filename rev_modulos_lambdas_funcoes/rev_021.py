from random import uniform
mat1 = [[round(uniform(0, 9), 1) for x in range(2)] for y in range(2)]
mat2 = [[round(uniform(0, 9), 1) for a in range(2)] for b in range(2)]
print('- ' * 15)
menu = input('Escolha a operação:\n'
             '[ a ] somar as matrizes\n'
             '[ b ] subtrair as matrizes\n'
             '[ c ] adicionar uma constante às matrizes\n'
             '[ d ] imprimir as matrizes\n'
             'Digite a opção: ').lower()[0]
while True:
    if menu in 'abcd':
        break
    else:
        menu = input('Opção inválida, tente novamente: ')
print('- ' * 15)
if menu == 'a':
    mat3 = [
        [round(mat1[lin][col] + mat2[lin][col], 1)
         for col in range(len(mat1[lin]))]
        for lin in range(len(mat1))
    ]
    for q in range(len(mat3)):
        for w in range(len(mat3)):
            print(f'{mat3[q][w]:^5}', end=' ')
        print()
elif menu == 'b':
    mat3 = [
        [round(mat1[lin][col] - mat2[lin][col], 1)
         for col in range(len(mat1[lin]))]
        for lin in range(len(mat1))
    ]
    for q in range(len(mat3)):
        for w in range(len(mat3)):
            print(f'{mat3[q][w]:^5}', end=' ')
        print()
elif menu == 'c':
    while True:
        try:
            num = int(input('Digite uma constante: '))
            break
        except ValueError:
            print('Valor inválido')
    mat3 = [
        [round(mat1[lin][col] * num, 1)
         for col in range(len(mat1[lin]))]
        for lin in range(len(mat1))
    ]
    mat4 = [
        [round(mat2[linha][coluna] * num, 1)
         for coluna in range(len(mat2[linha]))]
        for linha in range(len(mat2))
    ]
    for q in range(len(mat3)):
        for w in range(len(mat3)):
            print(f'{mat3[q][w]:^5}', end=' ')
        print(end=' ' * 10)
        for e in range(len(mat4)):
            print(f'{mat4[q][e]:^5}', end=' ')
        print()
else:
    for q in range(len(mat1)):
        for w in range(len(mat1)):
            print(mat1[q][w], end=' ')
        print(end=' ' * 10)
        for e in range(len(mat2)):
            print(mat2[q][e], end=' ')
        print()
