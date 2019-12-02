from random import randint
mat = [[randint(1, 9) for x in range(5)] for y in range(5)]
while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('Favor digitar somente números')
pos = []
ind = []
print('- ' * 15)
for l in range(len(mat)):
    for c in range(len(mat)):
        if num == mat[l][c]:
            ind = [l, c]
        print(mat[l][c], end=' ')
    if ind:
        pos.append(ind[:])
        ind.clear()
    print()
print('- ' * 15)
if pos:
    print(f'{num} foi encontrado na posição {pos}')
else:
    print(f'{num} não foi encontrado')
