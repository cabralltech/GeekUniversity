num = int(input('Valor: '))
if num % 3 == 0 or num % 5 == 0:
    print(f'{num} é divisível ou por 3 ou por 5')
else:
    print(f'{num} não é divisível por 3 nem por 5')
