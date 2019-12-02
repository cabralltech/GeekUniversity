def seg(ho, mi, se):
    se_ho = ho * 3600
    se_mi = mi * 60
    sec = se_ho + se_mi + se
    return f'A hora passada convertida em segundos é {sec}" '


# Programa Principal
horario = input('Horário HH:M:SS - ')
horario = horario.split(':')
hor = int(horario[0])
mins = int(horario[1])
segs = int(horario[2])
print(seg(hor, mins, segs))
