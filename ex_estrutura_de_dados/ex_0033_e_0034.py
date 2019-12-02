from random import randint
vetor = [randint(0, 10) for n in range(15)]
print(vetor)
for i, v in enumerate(vetor):
    if v == 0:
        value = vetor.pop(i-1)
        vetor.remove(0)
        vetor.append(value)
print(vetor)

vet = []
c = 0
while c < 10:
    num = randint(1, 99)
    if num not in vet:
        vet.append(num)
        c += 1
print(vet)
