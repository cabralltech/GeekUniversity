from random import uniform


def linha(x):
    print('- ' * x)


# vetor = [round(uniform(1, 9), 2) for x in range(10)]  list comprehension
vetor = list(
    map(lambda n: round(uniform(1, 9), 2),
        range(10))
)
print(vetor)
linha(5)
# vetor2 = [round(n ** 2, 2) for n in vetor]  list comprehension
vetor2 = list(
    map(
        lambda y: round(y ** 2, 2),
        vetor
    )
)
print(vetor2)
