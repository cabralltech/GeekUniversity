from random import randint


def linha(x):
    print('- ' * x)


# Programa Principal
vetor = [randint(1, 9) for c in range(8)]
print(vetor)
linha(5)
xis = int(input('Valor de 0 a 8: '))
yps = int(input('Valor de 0 a 8: '))
soma = vetor[xis] + vetor[yps]
linha(10)
print(soma)
