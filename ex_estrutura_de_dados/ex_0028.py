from random import randint
vetor = {randint(1, 99) for x in range(10)}
vetor1 = {num if num % 2 != 0 else randint(1, 99) for num in vetor}
vetor2 = {n if n % 2 == 0 else randint(1, 99) for n in vetor}
vetor3 = vetor & vetor1
vetor4 = vetor & vetor2
print('Vetor gerado: ')
print(vetor)
print('- ' * 5)
print('Ímpares do vetor e outros números')
print(vetor1)
print('- ' * 5)
print('Pares do vetor e outros números')
print(vetor2)
print('- ' * 5)
print('Utilizados nos ímpares')
print(vetor3)
print('- ' * 5)
print('Utilizados nos pares')
print(vetor4)
