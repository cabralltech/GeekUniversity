def maior(n1, n2):
    if n1 > n2:
        return f'{n1} é o maior número'
    return f'{n2} é o maior número'


# Programa Principal
num1 = int(input('Valor: '))
num2 = int(input('Valor: '))
print(maior(num1, num2))
