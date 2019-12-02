num1 = int(input('Valor: '))
num2 = int(input('Valor: '))
dif = 0
if num1 > num2:
    dif = num1 - num2
    print(f'{num1} é o maior e a diferença entre os dois é {dif}')
else:
    dif = num2 - num1
    print(f'{num2} é maior e a diferença entre os dois é {dif}')

numa = int(input('Valor: '))
numb = int(input('Valor: '))
if numa > numb:
    print(f'{numa} é maior que {numb}')
elif numa == numb:
    print(f'Eles são iguais')
else:
    print(f'{numb} é maior que {numa}')
