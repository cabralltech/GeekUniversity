def dentro_ret(v1, v2, p):
    if p[0] <= (v2[0] - v1[0]) and p[1] <= (v2[1] - v1[1]):
        return 1
    return 0


while True:
    try:
        x1 = int(input('"x" em vértice RET inferior esquerdo: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y1 = int(input('"y" em vértice RET inferior esquerdo: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
vet1 = x1, y1
print('- ' * 15)
while True:
    try:
        x2 = int(input('"x" em vértice RET superior direito: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y2 = int(input('"y" em vértice RET superior direito: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
vet2 = x2, y2
print('- ' * 15)
while True:
    try:
        x = int(input('"x" em ponto: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        y = int(input('"y" em ponto: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
ponto = x, y
print('- ' * 15)
print(dentro_ret(vet1, vet2, ponto))
