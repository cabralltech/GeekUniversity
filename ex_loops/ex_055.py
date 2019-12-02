n = int(input('Valor: '))
primo = None
cont = soma = total = 0
if n < 0:
    print('ERRO! Digite um número positivo: ')
else:
    print('- ' * 5)
    print(f'Os {n} primeiros números primos são:')
    print('- ' * 5)
    print('2 ', end='')
    np = 2
    while True:
        np += 1
        x = 2
        while x < np:
            if np % x == 0:
                primo = False
                break
            else:
                primo = True
            x += 1
        if primo:
            print(np, end=' ')
            cont += 1
            soma += np
        if cont == n - 1:
            break
total = soma + 2
print()
print('- ' * 5)
print(f'A soma deles é {total}')
