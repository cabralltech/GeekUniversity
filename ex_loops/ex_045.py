resp = 0
while resp != 3:
    resp = int(input('Escolha:\n'
                 '[ 1 ] km/h -› m/s\n'
                 '[ 2 ] ms -› km/h\n'
                 '[ 3 ] SAIR\n'
                 'Digite a opção: '))
    print('- ' * 15)
    if resp == 1:
        kms = float(input('Velocidade em km/h: '))
        print(f'{kms}km/h -› {kms / 3.6:.1f}m/s')
        print('- ' * 5)
    elif resp == 2:
        ms = float(input('Velocidade em m/s: '))
        print(f'{ms}m/s -› {ms * 3.6}km/h')
print('PROGRAMA ENCERRADO')
