num = 1
cont = maior = menor = 0
while num > 0:
    num = int(input('Valor: '))
    if cont == 0:
        maior = menor = num
    if cont > num > 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
