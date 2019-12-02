idade = int(input('Idade: '))
if 5 <= idade <= 7:
    print('INFANTIL A')
elif 8 <= idade <= 10:
    print('INFANTIL B')
elif 11 <= idade <= 13:
    print('JUVENIL A')
elif 14 <= idade <= 17:
    print('JUVENIL B')
elif idade >= 18:
    print('SÊNIOR')
else:
    print('Não aceitamos menores de 5 anos.')
