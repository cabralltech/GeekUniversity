sexo = input('Sexo: ').strip().upper()[0]
altura = float(input('Altura: '))
peso = 0
if sexo == 'M':
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso:.1f}')
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso:.1f}')
else:
    print(f'Sexo inválido')
