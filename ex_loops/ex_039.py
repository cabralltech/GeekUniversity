altura = float(input('Altura: '))
base = float(input('Base: '))
while base < 0 or altura < 0:
    altura = float(input('Altura: '))
    base = float(input('Altura: '))
area = (base * altura) / 2
print(f'A área do triângulo é {area:.1f}')
