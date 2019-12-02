from random import randint

mat = [[randint(1, 20) for x in range(4)] for y in range(4)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
# gten = list(map(lambda m: list(filter(lambda n: n > 10, m)), mat))
gten = [[n for n in m if n > 10] for m in mat]
# print(gten)
print('- ' * 15)
print(f'A quantidade de números > 10 na matriz é: {sum(map(lambda k: len(k), gten))}')
