def entre_soma(n1, n2):
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    num = [n for n in range(menor+1, maior)]
    return f'A soma dos números entre {menor} e {maior} é {sum(num)}'


# Programa Principal
num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))
print('- ' * 15)
print(entre_soma(num1, num2))
