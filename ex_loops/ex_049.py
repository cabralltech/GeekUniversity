carlos = 1
joao = 1/3
cont = 0
while joao < carlos:
    carlos += 0.02 * carlos
    joao += 0.05 * joao
    cont += 1
print(f'João com ultrapassa Carlos em {cont} meses')
