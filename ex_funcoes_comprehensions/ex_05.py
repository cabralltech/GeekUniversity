def volume(raio):
    vol = (4 * 3.1416 * (raio ** 3)) / 3
    return f'O volume da esfera de raio {raio} é: {vol:.1f}'


# Programa Principal
ra = float(input('Raio da esfera: '))
print(volume(ra))
