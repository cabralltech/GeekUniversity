maior = menor = 0
for i in range(1, 11):
    num = int(input('Valor: '))
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
