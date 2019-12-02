from random import randint


def des_pad(v):
    soma = somatorio = 0
    for i in v:
        soma += i
    media = soma / len(v)
    for c in v:
        somatorio += ((c - media) ** 2)
    desvio = (somatorio / (len(v) - 1)) ** 0.5
    return f'O desvio padrão do vetor acima é {desvio:.1f}'


vet = [randint(1, 10) for x in range(5)]
print(vet)
print(des_pad(vet))
