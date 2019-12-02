from random import randint
mat = [[randint(0, 5) for x in range(5)] for y in range(5)]
for lin in range(5):
    for col in range(5):
        print(f'{mat[lin][col]:^5}', end="")
    print()
ma_esq_dir = []
diagonal1 = []
diagonal2 = []
ma_cima_baixo = []
for li in range(5):
    for c in range(5):
        if c < 3:
            prod1 = prod3 = 1
            for p in range(3):
                prod1 *= mat[li][p+c]
            ma_esq_dir.append(prod1)
        if li < 3:
            prod2 = 1
            for p in range(3):
                prod2 *= mat[li+p][c]
            ma_cima_baixo.append(prod2)
        if li < 3 and c < 3:
            prod3 = 1
            for p in range(3):
                prod3 *= mat[li+p][c+p]
            diagonal1.append(prod3)
        if c > 1 and li < 3:
            prod4 = 1
            for p in range(3):
                prod4 *= mat[li+p][c-p]
            diagonal2.append(prod4)
diagonal = diagonal1 + diagonal2
print('- ' * 5)
print('Os maiores produtos possíveis:')
print(f'Da esquerda para a direita é: {max(ma_esq_dir)}')
print(f'De cima para baixo é: {max(ma_cima_baixo)}')
print(f'Na diagonal é: {max(diagonal)}')
