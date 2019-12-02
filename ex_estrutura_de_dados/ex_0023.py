from random import randint
a = [randint(1, 9) for x in range(5)]
b = [randint(1, 9) for y in range(5)]
escalar = [a[z] * b[z] for z in range(5)]
produto = sum(escalar)
print(a)
print('- ' * 10)
print(b)
print('- ' * 10)
print(f'O produto escalar dos dois conjuntos é {produto}')
