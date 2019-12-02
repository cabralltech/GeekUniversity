preco = float(input('Diigte o valor do produto: '))
total = 0
erro = False
uf = input('Diigte a sigla do estado de destino: ').upper().strip()
if uf == 'MG':
    total = preco + (preco * 0.07)
elif uf == 'SP':
    total = preco + (preco * 0.12)
elif uf == 'RJ':
    total = preco + (preco * 0.15)
elif uf == 'MS':
    total = preco + (preco * 0.08)
else:
    print('ERRO! Estado inávlido')
    erro = True
if not erro:
    print(f'O valor total do produto é R${total}')

