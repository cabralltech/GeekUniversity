altura = float(input('Altura: '))
peso = float(input('Peso: '))
clas = ' '
if peso < 60:
    if altura < 1.2:
        clas = 'A'
    elif 1.2 <= altura <= 1.7:
        clas = 'B'
    else:
        clas = 'C'
elif 60 <= peso <= 90:
    if altura < 1.2:
        clas = 'D'
    elif 1.2 <= altura <= 1.7:
        clas = 'E'
    else:
        clas = 'F'
else:
    if altura < 1.2:
        clas = 'G'
    elif 1.2 <= altura <= 1.7:
        clas = 'H'
    else:
        clas = 'I'
print(f'A pessoa cadastrada, de peso {peso}kg e {altura}m de altura está na categoria {clas}')
