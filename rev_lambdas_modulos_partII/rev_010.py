def maior(n1, n2):
    if n1 > n2:
        return f'{n1} é maior que {n2}'
    return f'{n2} é maior que {n1}'


while True:
    try:
        num1 = float(input('Primeiro valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        num2 = float(input('Segundo valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(maior(num1, num2))
