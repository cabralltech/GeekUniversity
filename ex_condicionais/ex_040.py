custo_fab = float(input('Custo de fábrica: '))
com = imp = total = 0
if custo_fab <= 12_000:
    com = custo_fab * 0.05
    total = custo_fab + com
elif 12_000 < custo_fab <= 25_000:
    com = custo_fab * 0.1
    imp = custo_fab * 0.15
    total = custo_fab + com + imp
else:
    com = custo_fab * 0.15
    imp = custo_fab * 0.2
    total = custo_fab + com + imp
print(f'O valor total do carro é de R${total:.2f}')
