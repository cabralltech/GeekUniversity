from random import randint
vet = []
cont = 0
while cont < 6:
    num = randint(1, 99)
    if num % 2 == 0:
        vet.append(num)
        cont += 1
print(vet)
print(vet[::-1])
