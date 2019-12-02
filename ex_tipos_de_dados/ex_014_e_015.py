graus = float(input('Ângulo em graus: '))
pi = 3.14
rad = graus * (pi / 180)
print(f'{graus}° -› {rad:.1f}rad')

rad = float(input('Ângulo em radianos: '))
graus = rad * (180 / pi)
print(f'{rad}rad -› {round(graus, 1)}°')
