from random import randint
c1 = c2 = 0
v1 = set()
v2 = set()
while c1 < 10:
    num = randint(1, 20)
    if num not in v1:
        v1.add(num)
        c1 += 1
while c2 < 10:
    n = randint(1, 20)
    if n not in v2:
        v2.add(n)
        c2 += 1
print(v1)
print('- ' * 15)
print(v2)
v3 = v1 | v2
print('- ' * 15)
print(v3)
