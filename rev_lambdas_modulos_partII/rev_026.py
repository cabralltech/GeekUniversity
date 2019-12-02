def somat(n):
    return sum(x for x in range(n+1))


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(somat(num))
