from random import randint


def linha(q):
    print('- ' * q)


vetor = [randint(1, 99) for x in range(10)]
print(vetor)
linha(5)
evens = [n for n in vetor if n % 2 == 0]
print(sorted(evens))
linha(5)
odds = list(
    filter(lambda c: c % 2 != 0,
           vetor)
)
print(sorted(odds))
