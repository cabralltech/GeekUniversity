from random import randint
a = [[randint(1, 9) for x in range(3)] for y in range(3)]
b = [[a[lin][col] ** 2 for col in range(3)] for lin in range(3)]
for l in range(3):
    for c in range(3):
        print(f'[{a[l][c]:^5}]', end=" ")
    print()
print('- ' * 15)
for li in range(3):
    for co in range(3):
        print(f'[{b[li][co]:^5}]', end=" ")
    print()
