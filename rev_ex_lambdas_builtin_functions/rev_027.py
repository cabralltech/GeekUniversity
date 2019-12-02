from random import randint


def primo(n):
    prime = False
    for x in range(2, n+1):
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
    return prime


# Programa Principal
vetor = [randint(1, 99) for c in range(10)]
prims = [p for p in vetor if primo(p)]
print(vetor)
print('- ' * 15)
print('PRIMOS:')
print('-' * 10)
for i in range(len(prims)):
    print(f'{prims[i]:<5}pos: {vetor.index(prims[i])}')
