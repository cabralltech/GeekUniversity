from random import randint
mat = [[randint(1, 20) for x in range(3)] for y in range(3)]
soma = []
for lin in range(3):
    for col in range(3):
        print(f'{mat[lin][col]:^4}', end="")
    print()
for s in range(3):
    so = 0
    for l in range(3):
        so += mat[l][s]
    soma.append(so)
print(soma)
