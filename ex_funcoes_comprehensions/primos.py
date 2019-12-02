def primo(num):
    primos = []
    for i in range(2, num):
        prime = True
        for x in range(2, i):
            if i % x == 0:
                prime = False
                break
        if prime:
            primos.append(i)
    return primos


# Programa Principal
numero = int(input('Valor: '))
print(primo(numero))
