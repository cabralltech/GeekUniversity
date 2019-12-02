x = 10
print(type(x))
y = x
if id(x) == id(y):
    print('x e y referenciam ao mesmo objeto')
    print(id(x), id(y), sep='-')
print(x is y)
x += 1
print(y, x, sep='-')
print(id(x))
print(id(y))
