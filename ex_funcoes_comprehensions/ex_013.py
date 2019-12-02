def oper(n1, n2, simb):
    operacao = {
        '+': n1 + n2,
        '-': n1 - n2,
        '*': n1 * n2,
        '/': n1 / n2
    }
    s = operacao.get(simb)
    return f'O resultado é {s:.1f}'


# Programa Principal
num1 = int(input('Valor: '))
num2 = int(input('Valor: '))
print('- ' * 10)
opera = input('Escolha a operação:\n'
              '[ + ] adição\n'
              '[ - ] subtração\n'
              '[ * ] multiplicação\n'
              '[ / ] divisão\n'
              'Digite a opção desejada: ')
print('- ' * 10)
print(oper(num1, num2, opera))
