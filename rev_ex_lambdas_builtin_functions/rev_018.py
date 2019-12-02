from random import randint
vetor = [randint(1, 99) for x in range(10)]
print('- ' * 15)
print(vetor)
num = int(input('Valor: '))
# mult = [n for n in vetor if n % num == 0] list comprehension
mult = list(filter(lambda n: n % num == 0, vetor))
print('- ' * 15)
print(mult)
