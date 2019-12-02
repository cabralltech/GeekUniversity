from random import randint


def soma_lin(m,l):
    soma = sum(m[l][x] for x in range(len(m[l])))
    return f'A soma dos elementos da linha {l} é {soma}'


mat = [[randint(1, 9) for a in range(6)] for b in range(7)]
for li in range(len(mat)):
    for co in range(len(mat[li])):
        print(mat[li][co], end=' ')
    print()
print('- ' * 15)
while True:
    try:
        linha = int(input('Escolha uma linha da matriz acima: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print('- ' * 15)
print(soma_lin(mat, linha))
