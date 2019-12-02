num = 1
quad = cubo = raiz = 0
while num > 0:
    num = int(input('Valor: '))
    quad = num ** 2
    cubo = num ** 3
    raiz = num ** 0.5
    print('- ' * 5)
    print(f'{num}exp2 = {quad}\n{num}exp3 = {cubo}\nRaiz quadrada de {num} = {raiz:.1f}')
    print('- ' * 5)
