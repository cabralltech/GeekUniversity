def media(n1, n2, n3, med):
    if med == 'a':
        return f'A média aritmética é {(n1 + n2 + n3) / 3:.1f}'
    return f'A média ponderada é {(n1 + (2 * n2) + (3 * n3))/ 6:.1f}'


# Programa Principal
no1 = float(input('Primeira nota: '))
no2 = float(input('Segunda nota: '))
no3 = float(input('Terceira nota: '))
me = input('Média a ser calculada:\n'
           '[ a ] aritmética\n'
           '[ p ] ponderada\n'
           'Digite a opção desejada: ').lower().strip()[0]
print(media(no1, no2, no3, me))
