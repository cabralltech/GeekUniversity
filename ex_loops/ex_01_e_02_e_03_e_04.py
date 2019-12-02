for i in range(3, 16, 3):
    print(i, end=' ')
print()

for i in range(1, 101, 3):
    print(i, end=' ')
print()

c = 1
while c <= 100:
    print(c, end=' ')
    c += 3
print()

c = 10
while c >= 0:
    print(c, end=' ')
    c -= 1
print('FIM!')

c = 0
while c <= 100_000:
    print(c , end=' ')
    c += 10_000
