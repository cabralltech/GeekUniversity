from random import randint
vetor1 = [randint(1, 9) for x in range(10)]
vetor2 = [randint(1, 9) for x in range(10)]
# vetor3 = [vetor1[n] + vetor2[n] for n in range(10)]  list comprehension
vetor3 = list(map(lambda n: vetor1[n] + vetor2[n], range(10)))
print(vetor1)
print('- ' * 15)
print(vetor2)
print('- ' * 15)
print(vetor3)
