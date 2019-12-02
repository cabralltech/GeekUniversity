cod = int(input('Código do produto: '))
qtd = int(input('Quantidade: '))
total = 0
erro = False
if cod == 100 or cod == 103:
    total = 1.2 * qtd
elif cod == 101:
    total = 1.3 * qtd
elif cod == 102:
    total = 1.5 * qtd
elif cod == 104:
    total = 1.7 * qtd
elif cod == 105:
    total = 2.2 * qtd
elif cod == 106:
    total = 1.0 * qtd
else:
    print('Produto inexistente')
    erro = True
if not erro:
    print(f'O valor total da compra é R${total:.2f}')
