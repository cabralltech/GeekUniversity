from random import uniform
vetor = [round(uniform(-10, 10), 1) for x in range(10)]
# neg = [n for n in vetor if n < 0]  list comprehension
neg = list(filter(lambda n: n < 0, vetor))
soma = sum(y for y in vetor if y >= 0)
print(vetor)
print('- ' * 15)
print(neg)
print('- ' * 15)
print(f'A soma dos valores positivos é {round(soma, 1)}')