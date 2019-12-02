from math import pi


def vol_esfera(r):
    return round((4 / 3) * pi * (r ** 3), 2)


raio = float(input('Raio: '))
print(vol_esfera(raio))
