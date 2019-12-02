from random import randint
vet = [randint(0, 50) for num in range(10)]
print(vet)
impares = [x for x in vet if x % 2 != 0]
print(impares)
for i, v in enumerate(impares):
    if i % 2 == 0:
        print(v, end=', ')
    else:
        print(v)

print('= ' * 10)
a = [randint(1, 99) for n in range(10)]
b = [randint(1, 99) for m in range(10)]
c = [a[y] - b[y] for y in range(10)]
print(a)
print(b)
print(c)
