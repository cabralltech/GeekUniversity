venda = float(input('Valor de venda mensal: '))
com = 0
perc_alta = venda * 0.16
perc = venda * 0.14
if venda > 100_000:
    com = 700 + perc_alta
elif 100_000 > venda >= 80_000:
    com = 650 + perc
elif 80_000 > venda >= 60_000:
    com = 600 + perc
elif 60_000 > venda >= 40_000:
    com = 550 + perc
elif 40_000 > venda >= 20_000:
    com = 500 + perc
else:
    com = 400 + perc
print(f'O total de vendas deste mês foi R$ {venda:.2f} - Comissão R${com:.2f}')
