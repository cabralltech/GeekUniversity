def fatoral(num):
    primos = []
    for i in range(2, num +1):
        prime = True
        for x in range(2, i):
            if i % x == 0:
                prime = False
                break
        if prime:
            primos.append(i)
    fat_pri = [n for n in primos if num % n == 0]
    return f'O maior fatorial de {num} é {max(fat_pri)}'


# Programa Principal
numero = int(input('Valor: '))
print(fatoral(numero))
