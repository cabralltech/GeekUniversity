n = int(input('Valor: '))
for i in range(0, n+1):
    print(i, end=' ')
print()
for i in range(n, -1, -1):
    print(i, end=' ')
print()
for i in range(0, n+1):
    if i % 2 == 0:
        print(i, end=' ')
print()
for i in range(n, -1, -1):
    if i % 2 == 0:
        print(i, end=' ')
