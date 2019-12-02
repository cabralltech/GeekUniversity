def triang(a, b, c):
    if abs(a - b) < c and abs(b - c) < a and abs(a - c) < b:
        if a == b and b == c:
            return f'Triângulo EQUILÁTERO'
        if a != b and b != c and c != a:
            return f'Triângulo ESCALENO'
        return f'Triângulo ISÓCELES'
    return f'Os lados {a}, {b} e {c} não formam um triângulo'


# Programa Principal
lado1 = float(input('Valor: '))
lado2 = float(input('Valor: '))
lado3 = float(input('Valor: '))
print('- ' * 10)
print(triang(lado1, lado2, lado3))
