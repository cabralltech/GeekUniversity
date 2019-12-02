def soma(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return f'A soma dos valores de 1 a {num} é {s}'


# Programa Principal
n = int(input('Valor: '))
print(soma(n))
