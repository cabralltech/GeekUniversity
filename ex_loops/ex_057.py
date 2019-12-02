a = int(input('Valor: '))
b = int(input('Valor: '))
primo = None
maior = menor = cont = 0
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
print('- ' * 15)
for i in range(menor, maior+1):
    for c in range(2, i):
        if i % c == 0:
            primo = False
            break
        else:
            primo = True
    if primo:
        print(i, end=' ')
        cont += 1
print()
print('- ' * 15)
print(f'Entre {menor} e {maior} existem {cont} números primos')
