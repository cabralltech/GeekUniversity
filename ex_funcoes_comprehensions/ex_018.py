def expon(x, z):
    return f'O valor {x} elevado a {z} é {x ** z}'


# Programa Principal
num = int(input('Valor: '))
exp = int(input('Exponencial: '))
print('- ' * 5)
print(expon(num, exp))
