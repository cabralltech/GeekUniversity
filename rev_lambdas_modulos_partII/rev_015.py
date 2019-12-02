def triangulo(a, b, c):
    print('- ' * 15)
    tri = False
    if (
            abs(a-b) < c < (a+b)
            and abs(b-c) < a < (b+c)
            and abs(c-a) < b < (c+a)
    ):
        tri = True
    if tri:
        print('Você formou um triângulo ', end='')
        if a != b != c:
            return 'ESCALENO'
        elif a == b == c:
            return 'EQUILÁTERO'
        return 'ISÓCELES'
    return 'Não é possível formar um triângulo com essas medidas'


while True:
    try:
        vl1 = int(input('Primeira medida: '))
        if vl1 > 0:
            break
        else:
            print('Valor deve ser > 0')
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        vl2 = int(input('Segunda medida: '))
        if vl2 > 0:
            break
        else:
            print('Valor deve ser > 0')
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        vl3 = int(input('Terceira medida: '))
        if vl3 > 0:
            break
        else:
            print('Valor deve ser > 0')
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(triangulo(vl1, vl2, vl3))
