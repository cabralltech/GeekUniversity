salario = float(input('Salário: '))
tempo = int(input('Tempo de serviço: '))
if salario <= 500:
    salario += (salario * 0.25)
    if tempo < 1:
        salario = salario
    elif tempo <= 3:
        salario += 100
    elif tempo <= 6:
        salario += 200
    elif tempo <= 10:
        salario += 300
    else:
        salario += 500
elif salario <= 1000:
    salario += (salario * 0.2)
    if tempo < 1:
        salario = salario
    elif tempo <= 3:
        salario += 100
    elif tempo <= 6:
        salario += 200
    elif tempo <= 10:
        salario += 300
    else:
        salario += 500
elif salario <= 1500:
    salario += (salario * 0.15)
    if tempo < 1:
        salario = salario
    elif tempo <= 3:
        salario += 100
    elif tempo <= 6:
        salario += 200
    elif tempo <= 10:
        salario += 300
    else:
        salario += 500
elif salario <= 2000:
    salario += (salario * 0.1)
    if tempo < 1:
        salario = salario
    elif tempo <= 3:
        salario += 100
    elif tempo <= 6:
        salario += 200
    elif tempo <= 10:
        salario += 300
    else:
        salario += 500
else:
    if tempo < 1:
        salario = salario
    elif tempo <= 3:
        salario += 100
    elif tempo <= 6:
        salario += 200
    elif tempo <= 10:
        salario += 300
    else:
        salario += 500
print(f'A partid o próximo mês, salário de R$ {salario:.2f}')
