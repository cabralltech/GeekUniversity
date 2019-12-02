def exclama(n):
    for i in range(n):
        print('!' * i)


while True:
    try:
        num = int(input('Número de linhas: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
exclama(num)
