def somatorio(vl1, vl2):
    if vl1 > vl2:
        maior = vl1
        menor = vl2
    else:
        maior = vl2
        menor = vl1
    return f'A soma dos números existentes entre {menor} e {maior} é ' \
        f'{sum(map(lambda x: x, range(menor+1, maior)))}'


while True:
    try:
        valor1 = int(input('Primeiro valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        valor2 = int(input('Segundo valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(somatorio(valor1, valor2))
