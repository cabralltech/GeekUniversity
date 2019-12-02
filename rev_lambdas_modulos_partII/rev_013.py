def oper(n1, n2, simb):
    print('- ' * 15)
    print('O resultado da operação é ', end='')
    if simb == '+':
        return n1 + n2
    elif simb == '-':
        return n1 - n2
    elif simb == '*':
        return n1 * n2
    return round(n1/n2, 1)


while True:
    try:
        num1 = int(input('Primeiro valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        num2 = int(input('Segundo valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        simbolo = input('Escolha a operação:\n'
                        '[ + ] adição\n'
                        '[ - ] subtração\n'
                        '[ * ] multiplicação\n'
                        '[ / ] divisão\n'
                        'Digite a opção: ')
        if simbolo not in '+-*/':
            print('\033[31mERRO! Operação inexistente\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Operação inexistente\033[m')
print(oper(num1, num2, simbolo))
