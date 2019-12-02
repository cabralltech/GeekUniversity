def volume(ra, alt):
    pi = 3.141592
    vol = pi * (ra ** 2) * alt
    return f'O volume do cilindro é {vol:.1f}'


# Programa Principal
raio = float(input('Raio do cilindro: '))
al = float(input('Altura do cilindro: '))
print(volume(raio, al))
