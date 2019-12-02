from random import randint
n = int(input('Quantas jogadas? '))
for i in range(0, n):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'd1 = {d1}\nd2 = {d2}')
    if d1 > d2:
        print(f'd1 > d2')
    elif d1 < d2:
        print(f'd1 < d2')
    else:
        print(f'd1 = d2')
    print('- ' * 5)
