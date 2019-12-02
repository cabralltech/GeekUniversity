a = input('Valor: ')
b = input('Valor: ')
a = list(a)
e = a.pop(-1)
a.insert(0, e)
b = list(b)
f = b.pop(-1)
b.insert(0, f)
a = [int(num) for num in a]
b = [int(n) for n in b]
print(a)
print(b)
c = [a[x] + b[x] for x in range(len(a))]
print(c)
