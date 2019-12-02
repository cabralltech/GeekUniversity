from random import randint
mat = [[0 for x in range(5)] for y in range(5)]
teste = []
lin = c = 0
for lin in range(5):
    while c < 5:
        num = randint(1, 99)
        if num not in teste:
            teste.append(num)
            mat[lin][c] = num
            c += 1
    c = 0
for ln in range(5):
    for co in range(5):
        print(f'{mat[ln][co]:^5}', end=" ")
    print()
