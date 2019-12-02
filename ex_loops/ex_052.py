print('= ' * 15)
print(f'{"MHILOCAS BANK":^30}')
print('= ' * 15)
saque = int(input('Valor para saque: '))
print('- ' * 15)
print('Você receberá:')
ced = 100
while True:
    cont = 0
    if saque >= ced:
        while saque >= ced:
            saque -= ced
            cont += 1
        print(f'{cont} notas de R$ {ced}')
    else:
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
    if saque == 0:
        break
print('- ' * 15)
print(f'{"OBRIGADA":^30}')
print('= ' * 15)
