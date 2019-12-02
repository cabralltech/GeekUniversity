from random import randint
vetor = [randint(-10, 10) for x in range(10)]
print(vetor)
print('- ' * 15)
neg = [0 if n < 0 else n for n in vetor]
print(neg)
