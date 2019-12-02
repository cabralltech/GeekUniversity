a = int(input('Valor: '))
b = int(input('Valor: '))
maior = menor = soma = 0
primo = None
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
print('- ' * 20)
for i in range(menor, maior+1):
    for c in range(2, i):
        if i % c == 0:
            primo = False
            break
        else:
            primo = True
    if primo:
        print(i, end=' ')
        soma += i
print()
print('- ' * 20)
print(f'A soma dos números primos entre {menor} e {maior} é {soma}')
