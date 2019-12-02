data = input('Data DD/MM/AAAA: ').strip()
data = data.split('/')
erro = False
if not data[0].isnumeric() and not data[1].isnumeric and not data[2].isnumeric():
    erro = True
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if dia < 30 and dia != 0:
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia > 29:
                erro = True
        else:
            if dia > 28:
                erro = True
else:
    erro = True
if mes > 12 and mes == 0:
    erro = True
if erro:
    print('Data inválida')
else:
    print('Data cadastrada')