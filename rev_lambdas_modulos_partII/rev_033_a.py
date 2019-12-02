def soma_fator(n):
    from math import factorial
    f = str(factorial(n))
    soma = sum(int(a) for a in f)
    return f'{n}! = {f} e a soma de seus algorismos é {soma}'


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(soma_fator(num))
