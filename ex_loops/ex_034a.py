def fatoral(num):
    primos = []
    for n in range(2, num+1):
        prime = True
        for x in range(2, n):
            if n % x == 0:
                prime = False
                break
        if prime:
            primos.append(n)
    exp = []




# Programa Principal
numero = int(input('Valor: '))
print(fatoral(numero))
