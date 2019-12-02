from random import uniform


def imprimir(v):
    print(v)


def inverso(v):
    print(v[::-1])


def media(v):
    media = sum(v) / len(v)
    return f'A média aritmética do vetor acima é {media:.2f}'


# Programa Principa;
vet = [round(uniform(1, 10), 2) for x in range(10)]
print('- ' * 15)
imprimir(vet)
print('- ' * 15)
inverso(vet)
print('- ' * 15)
print(media(vet))
