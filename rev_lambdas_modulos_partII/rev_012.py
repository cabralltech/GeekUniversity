def soma_alg():
    while True:
        try:
            n = int(input('Valor: '))
            if n > 0:
                break
            else:
                print('Digitar número > 0')
        except ValueError:
            print('\033[31mERRO! Valor inválido\033[m')
    n = str(n)
    return sum(map(lambda x: int(x), n))


print(soma_alg())
