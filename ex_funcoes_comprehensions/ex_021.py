def primos(num):
    pri = []
    for x in range(2, num):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break
        if prime:
            pri.append(x)
    return f'A quantidade de números primos abaixo de {num} é {len(pri)}\n{"- " * 15}\n{pri}'


# Programa Principal
numero = int(input('Valor: '))
print(primos(numero))
