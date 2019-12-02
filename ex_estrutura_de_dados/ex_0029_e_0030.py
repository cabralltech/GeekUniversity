from random import randint
vetor = {randint(1, 99) for x in range(10)}
print(vetor)
print('- ' * 15)
evens = {num for num in vetor if num % 2 == 0}
print(evens)
print(f'A soma de todos os números pares é {sum(evens)}')
print('- ' * 15)
odds = {nu for nu in vetor if nu % 2 != 0}
print(odds)
print(f'A quantidade de números ímpares é {len(odds)}')
print()

vetor1 = {randint(1, 20) for y in range(10)}
vetor2 = {randint(1, 20) for z in range(10)}
vetor3 = vetor1 & vetor2
print(vetor)
print('- ' * 15)
print(vetor1)
print('- ' * 15)
print(vetor2)
print('- ' * 15)
print(vetor3)
