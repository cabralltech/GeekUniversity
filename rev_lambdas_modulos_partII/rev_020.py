def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f'{n}! = {f}'


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(fatorial(num))
