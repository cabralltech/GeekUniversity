from math import ceil
horas = pag = mins = horaf = 0
hora_ent = int(input('Hora entrada: '))
min_ent = int(input('Minuto entrada: '))
hora_sai = int(input('Hora saída: '))
min_sai = int(input('Minuto saída: '))
tot_min_ent = (hora_ent * 60) + min_ent
tot_min_sai = (hora_sai * 60) + min_sai
total_min = tot_min_sai - tot_min_ent
if total_min > 60:
    horas = total_min / 60
    mins = int((horas - int(horas)) * 60)
    horaf = int(horas)
    horas = ceil(horas)
    if horas < 2:
        pag = 1.0 * horas
    elif 2 < horas < 4:
        horas -= 2
        pag = 2.0 + 1.4 * horas
    elif horas > 4:
        horas -= 4
        pag = 4.80 + 2.0 * horas
else:
    pag = 1.0
print(f'Entrada: {hora_ent}:{min_ent}\n'
      f'Saída: {hora_sai}:{min_sai}\n'
      f'Permanência: {horaf} hora(s) e {mins} minuto(s)\n'
      f'Total a pagar: R${pag:.2f}')
