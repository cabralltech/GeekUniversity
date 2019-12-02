kms = float(input('Distância: '))
gas = int(input('Litros de gasolina: '))
km_litro = kms / gas
print(f'Seu carro faz {km_litro:.1f}km/l')
if km_litro < 8:
    print('Venda o carro!')
elif 8 < km_litro < 14:
    print('ECONÔMICO')
else:
    print('SUPER ECONÔMICO!!!')
