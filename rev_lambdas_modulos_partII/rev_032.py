def simplifica(n, d):
    from math import gcd
    dc = gcd(n, d)
    nu = n // dc
    de = d //dc
    return f'A fração {n}/{d} simplificada é {nu}/{de}'


while True:
    try:
        nume = int(input('Numerador: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        deno = int(input('Denominador: '))
        if deno == 0:
            print('\033[31mERRO! Não existe divisão por zero\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(simplifica(nume, deno))
