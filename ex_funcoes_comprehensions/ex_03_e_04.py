def real(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


def quad(num):
    print(num ** 0.5)
    if num ** 0.5:
        return f'{num} é um quadrado perfeito'
    return f'{num} não é um quadrado perfeito'


numero = int(input('Valor: '))
print(real(numero))
print(quad(numero))