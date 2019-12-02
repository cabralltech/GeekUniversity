a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
opt = int(input('Escolha uma operação:\n'
                '[ 1 ] ADIÇÃO\n'
                '[ 2 ] SUBTRAÇÃO\n'
                '[ 3 ] MULTIPLICAÇÃO\n'
                '[ 4 ] DIVISÃO\n'
                'Digite a opção desejada: '))
if opt == 1:
    print(a + b)
elif opt == 2:
    print(a - b)
elif opt == 3:
    print(a * b)
elif opt == 4:
    print(round(a / b, 1))
else:
    print('Opção inválida')
