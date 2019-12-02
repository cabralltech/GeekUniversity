from random import randint


def maior_dez(m):
    mad = sum([len([b for b in li if b > 10]) for li in m])
    print(mad)
    return f'A matriz contém {mad} elementos maiores de 10'


mat = [[randint(1, 20) for a in range(4)] for b in range(4)]
for l in range(len(mat)):
    for c in range(len(mat)):
        print(f'{mat[l][c]:^5}', end=' ')
    print()
print('- ' * 15)
print(maior_dez(mat))
