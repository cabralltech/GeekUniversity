def hipot(cat1, cat2):
    return f'O valor da hipotenusa é {round((cat1 ** 2) + (cat2 ** 2) ** 0.5, 1)}'


while True:
    try:
        cateto1 = float(input('Cateto oposto: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        cateto2 = float(input('Cateto adjacente: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(hipot(cateto1, cateto2))
