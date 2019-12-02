from random import uniform


def imprimir(v):
    return v


def impr_inversa(v):
    return v[::-1]


def media_vet(v):
    return f'A média aritmética do vetor é {round(sum(v)/len(v), 1)}'


vet = [round(uniform(0, 10), 1) for x in range(15)]
print(imprimir(vet))
print('- ' * 15)
print(impr_inversa(vet))
print('- ' * 15)
print(media_vet(vet))
