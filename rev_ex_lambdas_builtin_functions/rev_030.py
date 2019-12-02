from random import randint
c = 0
va = set()
vb = set()
while c < 10:
    n = randint(1, 50)
    x = randint(1, 50)
    if n not in va and x not in vb:
        va.add(n)
        vb.add(x)
        c += 1
print(va)
print('- ' * 15)
print(vb)
print('- ' * 15)
vc = va & vb
print(vc)
