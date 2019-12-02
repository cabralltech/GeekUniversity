def fahr(c):
    return f'{round(c * (9/5) + 32, 1)}° F'


while True:
    try:
        celsius = float(input('Temperatura em Celsius: '))
        break
    except ValueError:
        print('\033[31mERRO! Temperatura inválida\033[m')
print(fahr(celsius))
