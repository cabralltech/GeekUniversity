num = int(input('Valor: '))
e = 1
for i in range(1, num+1):
    f = 1
    for c in range(1, i):
       f *= c
    e += 1 / f
    print(f, end=' ')
print(f'E({num}) == {e:.2f}')
