inicio = input('Inicio do teste hh:mm:ss -  ').strip()
duracao = int(input('Duração do teste em segundos -  '))
hora0 = int(inicio[:2])
min0 = int(inicio[3:5])
seg0 = int(inicio[6:])
hora1 = hora0 * 3600
min1 = min0 * 60
seg1 = seg0
total = hora1 + min1 + seg1 + duracao
hora = total / 3600
mins = (hora - int(hora)) * 60
seg = (mins - int(mins)) * 60
print(f'{int(hora)}:{int(mins)}:{int(seg)}')
