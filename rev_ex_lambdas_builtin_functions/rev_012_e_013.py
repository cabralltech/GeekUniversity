from random import randint

vetor = [randint(1, 9) for x in range(5)]
print(vetor)
print('- ' * 15)
print(f'O maior elementos é {max(vetor)}, '
      f'na pos. [{vetor.index(max(vetor))}]\nO menor é {min(vetor)}, '
      f'na pos. [{vetor.index(min(vetor))}]')
media = sum(vetor) / len(vetor)
print(f'A média dos valores é {round(media, 1)}')
