from random import randint


def vetor(n):
    c = 0
    while c < 10:
        x = randint(1, 100)
        if x not in n:
            n.append(x)
            c += 1
    return n


# Programa Principal
num = []
print(vetor(num))
