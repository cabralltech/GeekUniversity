def som(num):
    nums = [((x ** 2) + 1) / (x + 3) for x in range(1, num+1)]
    soma = 0
    for i in nums:
        soma += i
    return f'A soma dos valores da expressão dada é {soma:.2f}'


# Programa Principal
numero = int(input('Valor: '))
print(som(numero))
