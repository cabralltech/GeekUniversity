peso = float(input('Peso em kg: '))
altura = float(input('Altura em metros: '))
imc = peso / (altura ** 2)
con = ' '
if imc <= 18.5:
    con = 'ABAIXO DO PESO'
elif imc < 25:
    con = 'SAUDÁVEL'
elif imc < 30:
    con = 'PESO EM EXCESSO'
elif imc < 35:
    con = 'OBESIDADE GRAU I'
elif imc < 40:
    con = 'OBESIDADE GRAU II (severa)'
else:
    con = 'OBESIDADE GRAU II (mórbida)'
print(f'{altura}m e {peso}kg - {con}')
