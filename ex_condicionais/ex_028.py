x = int(input('Valor: '))
y = int(input('Valor: '))
z = int(input('Valor: '))
media = 0
m = ''
erro = False
opt = input('Escolha uma das médias:\n'
            'a) Geométrica\n'
            'b) Ponderada\n'
            'c) Harmônica\n'
            'd) Aritmética\n'
            'Digite a opção desejada: ').strip().lower()[0]
if opt == 'a':
    media = (x * y * z) ** (1 / 3)
    m = 'Geométrica'
elif opt == 'b':
    media = (x + 2 * y + 3 * z) / 6
    m = 'Ponderada'
elif opt == 'c':
    media = 1 / ((1 / x) + (1 / y) + (1 / z))
    m = 'Harmônica'
elif opt == 'd':
    media = (x + y + z) / 3
    m = 'Aritmética'
else:
    print('Opção inválida')
    erro = True
if not erro:
    print(f'Média {m} = {media:.1f}')
