def troque(a, b):
    aux = a
    a = b
    b = aux
    return f'Era: a) {b} e b) {a}\nAgora a) {a} e b) {b}'

while True:
    try:
        n1 = int(input('Valor1: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
while True:
    try:
        n2 = int(input('Valor2: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
print(troque(n1, n2))
