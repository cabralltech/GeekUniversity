n = cont = contpar = 0
while n != 1000:
    n = int(input('Valor: '))
    if n != 1000:
        cont += 1
    if n % 2 == 0 and n != 1000:
        contpar += 1
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')
print(f'Foram digitados {cont} números, dos quais {contpar} são pares')
