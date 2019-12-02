from random import randint
a = [[randint(1, 9) for x in range(3)] for y in range(3)]
b = [[randint(1, 9) for s in range(3)] for t in range(3)]
c = [[a[lin][col] * b[lin][col] for col in range(3)] for lin in range(3)]
for l in range(3):
    for cn in range(3):
        print(f'[{a[l][cn]:^5}]', end=" ")
    print()
print('- ' * 15)
for li in range(3):
    for co in range(3):
        print(f'[{b[li][co]:^5}]', end=" ")
    print()
print('- ' * 15)
for lh in range(3):
    for cl in range(3):
        print(f'[{c[lh][cl]:^5}]', end=" ")
    print()
