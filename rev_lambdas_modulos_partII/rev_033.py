def fatorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


def soma_fat(n):
    fat = str(fatorial(n))
    soma = sum(int(a) for a in fat)
    return f'{n}! = {fat} e a soma de seus algorismos é {soma}'


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(soma_fat(num))
