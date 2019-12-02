cont = soma = media = maior = menor = som_pares = med_pares = c_par = 0
while True:
    num = int(input('Valor: '))
    soma += num
    if num % 2 == 0:
        c_par += 1
        som_pares += num
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    resp = ' '
    while resp not in 'NS':
        resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break
media = soma / cont
med_pares = som_pares / c_par
print('- ' * 15)
print(f'a) A soma dos valores digitados é {soma}\n'
      f'b) A quantidade de valores digitados é {cont}\n'
      f'c) A média dos valores digitados é {media:.1f}\n'
      f'd) O maior valor digitado é {maior}\n'
      f'e) O menor valor digitado é {menor}\n'
      f'f) A média dos valores pares é {med_pares:.1f}')
