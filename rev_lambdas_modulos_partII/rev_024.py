def piramide(n):
    ast = 1
    esp = n
    for i in range(n):
        for x in range(esp, -1, -1):
            print(' ', end='')
        print('*' * ast)
        ast += 2
        esp -= 1


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
piramide(num)
