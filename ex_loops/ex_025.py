soma = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(f'A soma dos múltiplos de 3 ou 5 de 0 a 1000 é {soma}')
