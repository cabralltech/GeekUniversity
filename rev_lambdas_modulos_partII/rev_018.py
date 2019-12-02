def expon(x, z):
    return f'O resultado é {x ** z}'


while True:
    try:
        xis = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        ze = int(input('Valor exponencial: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(expon(xis, ze))
