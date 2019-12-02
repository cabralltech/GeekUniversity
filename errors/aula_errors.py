while True:
    try:
        num = int(input('Valor: '))
    except (TypeError, ValueError):
        print('Por favor, somente números')
    else:
        print(f'Você digitou {num}')
        break

while True:
    try:
        nome = input('Nome completo: ')
    except (ValueError, TypeError):
        print('Nome inválido')
    else:
        print(f'Seu nome é {nome}')
        break
