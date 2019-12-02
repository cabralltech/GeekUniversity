antigo = float(input('Preço antigo: R$ '))
novo = 0
msg = ' '
if antigo < 50:
    novo = antigo + (antigo * 0.05)
elif 50 <= antigo <= 100:
    novo = antigo + (antigo * 0.1)
else:
    novo = antigo + (antigo * 0.15)
if novo < 80:
    msg = 'BARATO'
elif 80 <= novo <= 120:
    msg = 'NORMAL'
elif 120 < novo <= 200:
    msg = 'CARO'
else:
    msg = 'MUITO CARO'
print(f'O produto de R${antigo:.2f} passa para R${novo:.2f} e é {msg}')
