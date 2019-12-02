from random import randint
v1 = [randint(1, 9) for x in range(10)]
v2 = [randint(1, 9) for y in range(10)]
v3 = [v1[n] if not n % 2 else v2[n] for n in range(10)]
print(v1)
print('- ' * 15)
print(v2)
print('- ' * 15)
print(v3)
