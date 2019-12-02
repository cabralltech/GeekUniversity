def exp_fat(n):
    x = n
    for i in range(n-1, 1, -1):
        x **= i
    return f'O fatorial exponencial de {n} é {x}'


# Programa Principal
num = int(input('Valor: '))
print(exp_fat(num))
