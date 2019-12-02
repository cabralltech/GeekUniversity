from random import randint
matriz = [[randint(10, 99) for x in range(5)]for y in range(5)]
num = int(input('Digite um valor de 10 a 99: '))
found = False
count = 0
pos = []
duplicado = []
for lin in range(5):
    for col in range(5):
        if num == matriz[lin][col]:
            pos.append(lin)
            pos.append(col)
            found = True
            count += 1
print('- ' * 5)
if found:
    print(f'O número {num} está na posição {pos[0]},{pos[1]}')
else:
    print(f'O número {num} não foi encontrado')
print('- ' * 5)
for l in range(5):
    for c in range(5):
        if matriz[l][c] == num:
            matriz[l][c] = f'\033[34m{matriz[l][c]}\033[m'
        print(matriz[l][c], end=' ')
    print()
