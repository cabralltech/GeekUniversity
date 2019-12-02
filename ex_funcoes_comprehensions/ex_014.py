def eco(km, lt):
    consumo = km / lt
    if consumo < 8:
        return f'Venda o carro!'
    elif consumo < 14:
        return f'Econômico'
    elif consumo > 12:
        return f'Super econômico'


# Programa Principal
qui = float(input('Distância percorrida: '))
litros = float(input('Gasolina consumida em litros: '))
print('- ' * 10)
print(eco(qui, litros))
