def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def senh_taylor(ang):
    from math import pi
    rad = ang * (pi/180)
    senh = sum(map(lambda x: (rad ** ((2*x)+1)) / fat((2*x)+1), range(6)))
    return f'O seno hiperbólico de {ang}° é {round(senh, 2)}'


while True:
    try:
        angulo = float(input('Ângulo: '))
        break
    except ValueError:
        print('\033[31mERRO! Ângulo inexistente\033[m')
print(senh_taylor(angulo))
