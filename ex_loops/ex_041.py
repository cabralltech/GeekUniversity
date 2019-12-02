r1 = int(input('Resistor 1: '))
r2 = int(input('Resistor 2: '))
r = 0
while r1 != 0 != r2:
    r = (r1 * r2) / (r1 + r2)
    print(f'O paralelo entre {r1} e {r2} é {r:.1f}')
    print('Digite novos valores')
    r1 = int(input('Resistor 1: '))
    r2 = int(input('Resistor 2: '))
print('PROGRAMA ENCERRADO')
