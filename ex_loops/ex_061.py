prod = pali = maior = cont = 0
pal = inverso = ' '
for i in range(101, 1000):
    for c in range(100, i):
        prod = c * i
        pal = str(prod)
        inverso = pal[::-1]
        cont = 0
        if pal == inverso:
            pali = int(pal)
            cont += 1
    if cont == 1:
        maior = pali
    else:
        if pali > maior:
            maior = pali
print('- ' * 15)
print(f'O maior palíndromo resultante de um produto \n'
      f'de dois números de três dígitos é {maior}')
print('- ' * 15)
