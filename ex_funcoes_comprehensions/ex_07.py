def fahr(temp):
    fa = temp * (9 / 5) + 32
    return f'{temp}°C equivale a {fa:.1f}°F'


# Programa Principal
celsius = float(input('Temperatura em Celsius: '))
print(fahr(celsius))
