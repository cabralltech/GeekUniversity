def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def cosh_taylor(ang):
    from math import pi
    rad = ang * (pi/180)
    cosh = sum(map(lambda x: (rad ** (2*x)) / fat(2*x), range(6)))
    return f'O cosseno hiperbólico de {ang}° é {round(cosh, 2)}'


while True:
    try:
        angulo = float(input('Ângulo: '))
        break
    except ValueError:
        print('\033[31mERRO! Ângulo inexistente\033[m')
print(cosh_taylor(angulo))
