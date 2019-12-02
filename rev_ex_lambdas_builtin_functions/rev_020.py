from random import randint
vetor = [randint(0, 50) for x in range(10)]
impares = [n for n in vetor if n % 2 == 1]
print('- ' * 5)
for i in range(len(vetor)):
    if i < len(impares):
        print(vetor[i], impares[i])
    else:
        print(vetor[i])
