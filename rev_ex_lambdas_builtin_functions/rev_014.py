from random import randint
vetor = [randint(1, 9) for x in range(10)]
# iguais = {n for n in vetor if vetor.count(n) > 1}  set comprehension
iguais = set(filter(lambda n: vetor.count(n) > 1, vetor))
print(vetor)
print('- ' * 15)
print(iguais)
