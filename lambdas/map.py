from math import pi


def area_circ(r):
    """Returns the area of a circle"""
    return pi * (r ** 2)


# Programa Principal
print(f'A área de um círculo de raio 5cm é {round(area_circ(5), 1)}')
raios = [4, 7.6, 2.8, 3, 5.2]
areas = list(map(lambda n: round(area_circ(n), 1), raios))
print(areas)


cidades = [('Tóquio', 23), ('Londres', 14), ('Nova Iorque', 25), ('Calcutá', 36), ('Aucklan', 13)]
temp_fah = list(map(lambda c: (c[1] * 9/5) + 32, cidades))
print(temp_fah)
