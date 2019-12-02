def primo(a):
    pri = True
    for i in range(2, a):
        if a % i == 0:
            pri = False
    return pri


#Programa Principal
from random import randint
vetor = [randint(1, 99) for num in range(10)]
print(vetor)
for i, n in enumerate(vetor):
    if primo(n):
        print(f'Número primo {n} - posição {i}')


