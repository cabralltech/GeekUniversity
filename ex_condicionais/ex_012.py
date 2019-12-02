from math import log
num = int(input('Valor: '))
if num > 0:
    print(f'O logaritmo de {num} é {log(num):.2f}')
else:
    print('Número inválido')
