from random import randint, uniform


def maior(v):
    return f'{vet}\n{"- " * 15}\nO maior elemento é {max(vet)}'


def media(ve):
    med = round(sum(ve) / len(ve), 1)
    return f'{ve}\n{"- " * 15}\nA média dos elementos é {med}'


vet = [randint(1, 99) for x in range(randint(5, 20))]
print(maior(vet))
print('- ' * 5)
print('- ' * 5)
vetor = [round(uniform(0, 10), 1) for y in range(randint(5, 20))]
print(media(vetor))
