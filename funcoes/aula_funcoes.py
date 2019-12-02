from random import randint
instrutor = 'Geek'

def cantar_parabens():
    print('Parabéns pra você\n' * 2, end='')
    print('Parabéns caro amigo')
    print('Parabéns pra você')


def oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'

cantar = cantar_parabens
cantar()

num = [print(x, end=' ') for x in range(1, 51) if x % 2 == 0]  # discouraged
# better not to use print inside list comprehensions
print()
print(oi())
print(instrutor)


