def fat_duplo(num):
    f = 1
    for i in range(1, num+1):
        if i % 2 != 0:
            f *= i
    return f'O fatorial duplo de {num} é {f}'


# Programa Principal
while True:
    numero = int(input('Valor: '))
    if numero > 0 and numero % 2 != 0:
        break
    else:
        print('\033[31mERRO! Digite um valor ímpar, maior que 0\033[m')
        print('- ' * 5)
print('- ' * 15)
print(fat_duplo(numero))
