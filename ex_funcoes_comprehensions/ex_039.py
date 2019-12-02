def troque(a, b):
    aux = b
    b = a
    a = aux
    return f'Agora Valor1 é {a} e Valor2 é {b}'


# Programa Principal
num1 = int(input('Valor1: '))
num2 = int(input('Valor2: '))
print(troque(num1, num2))
