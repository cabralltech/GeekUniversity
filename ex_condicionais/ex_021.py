a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
opt = int(input('Escolha a operação:\n'
                '[ 1 ] SOMA\n'
                '[ 2 ] SUBTRAÇÃO\n'
                '[ 3 ] MULTIPLICAÇÃO\n'
                '[ 4 ] DIVISÃO\n'
                'Digite a opção desejada: '))
if opt == 1:
    print(a + b)
elif opt == 2:
    if a > b:
        print(a - b)
    else:
        print(b - a)
elif opt == 3:
    print(a * b)
elif opt == 4:
    if a > b != 0:
        print(round(a / b, 2))
    elif b > a != 0:
        print(round(b / a, 2))
    else:
        print('Não se pode realizar a divisão, porque o denominador é igual a 0')
else:
    print('Opção inválida')
