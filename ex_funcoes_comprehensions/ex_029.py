def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def senh_taylor(ang):
    from math import pi
    rad = ang * (pi / 180)
    taylor = [(rad ** ((2*x)+1) / fat((2*x)+1)) for x in range(6)]
    soma = 0
    for c in taylor:
        soma += c
    return f'A série de Taylor para o seno de {ang}°:\n{taylor}\nSeno hiperbólico = {soma:.2f}'


# Programa Principal
angulo = float(input('Ângulo: '))
print(senh_taylor(angulo))
