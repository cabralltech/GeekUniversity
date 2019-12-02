def soma(num):
    if int(num) > 0:
        nu = [int(n) for n in num]
        som = sum(nu)
        return f'A soma dos algorismos de {num} é {som}'
    return 'Número inválido'


# Programa Principal
numero = input('Valor: ')
print(soma(numero))
