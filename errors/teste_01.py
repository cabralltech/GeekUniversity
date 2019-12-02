def leiadin(msg):
    while True:
        n = input(msg)
        try:
            return float(n.replace(',', '.'))
        except ValueError:
            print('\033[31mValor inválido!\033[m')


# Programa Principal
d = leiadin('Valor: ')
print(d)
