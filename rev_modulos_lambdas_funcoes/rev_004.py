from random import randint

mat = [[randint(10, 50) for x in range(4)] for y in range(4)]
maior = max(map(lambda m: max(m), mat))
pos = []
for l in range(len(mat)):
    for c in range(len(mat)):
        if mat[l][c] == maior:
            pos = [l, c]
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
print(f'O maior elemento da matriz é {maior} e está a posicão {pos}')
