preco = float(input('Valor produto: '))
avista = preco - (preco * (10/100))
parcela = preco / 3
com_a_vista = avista * 0.05
com_parcela = preco * 0.05
print(f'Valor do produto à vista com 10% desconto: R${avista:.2f}')
print(f'Valor da parcela para 3x: R${parcela:.2f}')
print(f'Comissão para venda à vista: R${com_a_vista:.2f}')
print(f'Comissão para venda parcelada: R${com_parcela:.2f}')
