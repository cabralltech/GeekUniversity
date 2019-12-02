from random import randint
vetor = [randint(0, 10) for x in range(15)]
vet_comp = list(filter(lambda n: n != 0, vetor))
print(vetor)
print('- ' * 15)
print(vet_comp)
