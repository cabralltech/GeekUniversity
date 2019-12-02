def vetor(v):
    from random import randint
    c = 0
    while c < randint(5, 10):
        n = randint(1, 99)
        if n not in v:
            v.append(n)
            c += 1
    return v


vet = []
print(vetor(vet))
