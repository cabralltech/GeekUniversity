def consumo(dist, gaso):
    con = round(dist/gaso, 1)
    if con < 8:
        return f'O carro faz {con}km/l - VENDA O CARRO!'
    elif 8<= con <= 14:
        return f'O carro faz {con}km/l - CARRO ECONÔMICO'
    return f'O carro faz {con}km/l - CARRO SUPER ECONÔMICO'


while True:
    try:
        distancia = float(input('Distância percorrida: '))
        break
    except ValueError:
        print('\033[31mERRO! Distância inválida\033[m')
while True:
    try:
        gasolina = float(input('Gasolina em litros: '))
        break
    except ValueError:
        print('\033[31mERRO! Quantidade inválida\033[m')
print(consumo(distancia, gasolina))
