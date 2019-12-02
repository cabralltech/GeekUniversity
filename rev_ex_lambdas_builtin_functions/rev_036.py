from random import uniform
vet = [round(uniform(1, 9), 1) for x in range(10)]
print(vet)
print('- ' * 10)
print(sorted(vet))
