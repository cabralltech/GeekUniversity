from math import pi


def vol_cil(r, h):
    return f'O volume do cilindro é {round(pi * (r**2) * h, 1)}'


while True:
    try:
        raio = float(input('Raio do cilindro: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        altura = float(input('Altura do cilindro: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(vol_cil(raio, altura))
