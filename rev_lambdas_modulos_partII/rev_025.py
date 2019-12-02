def somat(n):
    return sum(map(lambda x: ((x**2)+1)/(x+3), range(1, n+1)))


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(round(somat(num), 2))
