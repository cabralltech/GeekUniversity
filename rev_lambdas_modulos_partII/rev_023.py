def lat_tri(n):
    for i in range(n+1):
        print('*' * i)
    for x in range(n-1, 0, -1):
        print('*' * x)


while True:
    try:
        num = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
lat_tri(num)
