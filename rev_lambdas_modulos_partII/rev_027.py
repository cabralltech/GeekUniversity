def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def sen_taylor(ang):
    from math import pi
    rad = ang * (pi/180)
    sen = sum(map(lambda x: (((-1) ** x)/fat((2*x)+1) * (rad ** ((2*x) + 1))), range(6)))
    return f'O seno de {ang} é {round(sen, 2)}'


while True:
    try:
        angulo = float(input('Ângulo em graus: '))
        break
    except ValueError:
        print('\033[31mERRO! Ângulo inexistente\033[m')
print(round(sen_taylor(angulo), 2))
