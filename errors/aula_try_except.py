def divide(a, b):
    try:
        return round(float(a) / float(b), 1)
    except ValueError:
        print('Favor digitar somente números')
    except ZeroDivisionError:
        print('Não existe divisão por 0')


while True:
    n1 = input('Valor: ')
    n2 = input('Valor: ')
    res = divide(n1, n2)
    if type(res) is float:
        break
print(res)
