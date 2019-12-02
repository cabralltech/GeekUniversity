from random import randint
vet = [randint(1, 99) for x in range(6)]
pares = [n for n in vet if n % 2 == 0]
print(vet)
print('- ' * 10)
print(pares)
print(f'A soma dos números pares é {sum(pares)}')
impares = list(filter(lambda y: y % 2 ==1, vet))
print('- ' * 10)
print(impares)
print(f'A quantidade de números ímpares é {len(impares)}')
