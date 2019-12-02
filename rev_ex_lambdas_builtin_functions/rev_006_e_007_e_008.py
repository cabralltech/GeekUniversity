from random import randint

vetor = [randint(1, 9) for x in range(10)]
print(vetor)
print('- ' * 15)
print(f'O menor elemento é {min(vetor)} na pos. {vetor.index(min(vetor))}')
print(f'O maior elemento é {max(vetor)} na pos. {vetor.index(max(vetor))}')
print('- ' * 15)
vetor2 = [randint(1, 9) for y in range(6)]
print(vetor2)
print('- ' * 15)
print(vetor2[::-1])
