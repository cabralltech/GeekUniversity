km_hora = float(input('Velocidade em quilômetros por hora: '))
ms_segundo = km_hora / 3.6
print(f'{km_hora}km/h -› {ms_segundo:.1f}m/s')

ms_segundo = float(input('Velocidade em metros por segundo: '))
km_hora = ms_segundo * 3.6
print(f'{ms_segundo}m/s -› {km_hora}km/h')