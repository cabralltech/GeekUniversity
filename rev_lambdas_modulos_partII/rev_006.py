def segundos():
    while True:
        try:
            h = int(input('Horas: '))
            if 0 <= h <= 24:
                break
            else:
                print('Hora inválida')
        except ValueError:
            print('Digitar somente números')
    while True:
        try:
            m = int(input('Minutos: '))
            if 0 <= m <= 60:
                break
            else:
                print('Minuto inválido')
        except ValueError:
            print('Digitar somente números')
    while True:
        try:
            s = int(input('Segundos: '))
            if 0 <= s <= 60:
                break
            else:
                print('Segundo inválido')
        except ValueError:
            print('Digitar somente números')
    return f'O horário passado foi {h}h, {m}min e {s}s, equivalente a {(h*3600) + (m*60) + s} segundos'


print(segundos())
