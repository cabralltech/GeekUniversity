def media(nt1, nt2, nt3, m='a'):
    if m == 'a':
        return f'A média aritimética do aluno é {round((nt1 + nt2 + nt3)/ 3, 1)}'
    return f'A média ponderada do aluno é {round((5*nt1 + 3*nt2 + 2*nt3)/ 10, 1)}'


while True:
    try:
        nota1 = float(input('Primeira nota: '))
        break
    except ValueError:
        print('\033[31mERRO! Nota inválida\033[m')
while True:
    try:
        nota2 = float(input('Segunda nota: '))
        break
    except ValueError:
        print('\033[31mERRO! Nota inválida\033[m')
while True:
    try:
        nota3 = float(input('Terceira nota: '))
        break
    except ValueError:
        print('\033[31mERRO! Nota inválida\033[m')
while True:
    med = input('Escolha a média:\n'
                '[ a ] aritmética\n'
                '[ p ] ponderada\n'
                'Digite a opção: ').lower().strip()[0]
    if med in 'ap':
        break
    else:
        print('\033[31mERRO! Média inválida\033[m')
print(media(nota1, nota2, nota3, med))
