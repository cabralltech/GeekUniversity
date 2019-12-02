def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def cos_taylor(ang):
    from math import pi
    rad = ang * (pi/180)
    coss = sum(map(lambda x: (((-1) ** x)/fat(2*x)) * (rad ** (2*x)), range(6)))
    if round(coss, 2) == 0:
        coss = abs(coss)
    return f'O cosseno de {ang}° é {round(coss, 2)}'


while True:
    try:
        angulo = float(input('Ângulo: '))
        break
    except ValueError:
        print('\033[31mÂngulo inexistente\033[m')
print(cos_taylor(angulo))
