hab = int(input('Total de habitantes da cidade: '))
kwh= float(input('Valor do kwh: '))
consumo = media = tot_res = tot_ind = tot_com = maior = menor = cod = soma = 0
for p in range(1, hab+1):
    consumo = int(input(f'Consumo hab {p}: '))
    soma += consumo
    if p == 1:
        maior = menor = consumo
    else:
        if consumo > maior:
            maior = consumo
        if consumo < menor:
            menor = consumo
    cod = int(input('Código de consumo: '))
    if cod == 1:
        tot_res += consumo * kwh
    elif cod == 2:
        tot_ind += consumo * kwh
    else:
        tot_com += consumo * kwh
media = soma / hab
print('- ' * 15)
print(f'O maior consumo da cidade "X" é {maior}kwh\n'
      f'O menor consumo da cidade "X" é {menor}kwh\n'
      f'A média de consumo é {media}kwh\n'
      f'Total Residencial: R$ {tot_res:.2f}\n'
      f'Total Indústria: R$ {tot_ind:.2f}\n'
      f'Total Comércio: R$ {tot_com:.2f}')
