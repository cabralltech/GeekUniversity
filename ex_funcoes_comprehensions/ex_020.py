def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return f'{num}! = {fat}'


# Programa Principal
numero = int(input('Valor: '))
print(fatorial(numero))
