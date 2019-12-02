maior = 0
for i in range(0, 2):
    num = int(input('Valor: '))
    if i == 0:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'O maior número digitado foi {maior}')

n = int(input('Valor: '))
rq = 0
if n > 0:
    rq = n ** 0.5
    print(f'A raiz quadrada de {n} é {rq}')
else:
    print(f'{n} é um número inválido')

numero = int(input('Valor: '))
rq = quad = 0
if numero > 0:
    rq = n ** 0.5
    print(f'A raiz quadrada de {numero} é {rq}')
else:
    quad = numero ** 2
    print(f'O quadrado de {numero} é {quad}')

real = int(input('Valor: '))
rq = quad = 0
if real > 0:
    rq = real ** 0.5
    quad = real ** 2
    print(f'A raiz quadrada de {real} é {rq} e {real} ao quadrado é {quad}')
