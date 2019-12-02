def soma(a, b):
    return a + b


def subt(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def calcular(a, b, func):
    return func(a, b)


n1, n2 = 8, 4
print('- ' * 15)
print(calcular(n1, n2, soma))
print('- ' * 5)
print(calcular(n1, n2, subt))
print('- ' * 5)
print(calcular(n1, n2, mult))
print('- ' * 5)
print(calcular(n1, n2, div))

