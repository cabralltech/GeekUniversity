n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
menor = maior = soma = 0
produto = 1
if n1 < n2:
    menor = n1
    maior = n2
else:
    menor = n2
    maior = n1
for i in range(menor, maior+1):
    if i % 2 == 0:
        print(i, end=' ')
        soma += i
print()
for i in range(menor, maior+1):
    if i % 2 != 0:
        produto *= i
        print(i, end=' ')
print()
print(f'A soma dos números pares entre {menor} e {maior} é {soma}\n'
      f'O produto dos números ímpares entre {menor} e {maior} é {produto}')
