c = maior = cm = 0
while True:
    num = int(input('Valor: '))
    if c == 0:
        maior = num
    else:
        if num > maior:
            maior = num
    c += 1
    if num == maior:
        cm += 1
    resp = ' '
    while resp not in 'NS':
        resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break
print(f'O maior número digitado foi {maior} e ele foi digitado {cm - 1} vez(es)')
