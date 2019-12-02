from random import choice
resp = ['a', 'b', 'c', 'd']
gabarito = [choice(resp) for x in range(10)]
print('Gabarito: ', end='   ')
for v in gabarito:
    print(v, end=' ')
print()
print('- ' * 15)
mat = [[choice(resp) for a in range(10)] for al in range(5)]
n = nu = 1
for l in mat:
    print(f'Estudante {n}: ', end='')
    for c in l:
        print(c, end=' ')
    print()
    n += 1
print('- ' * 15)
for li in mat:
    res = len(list(filter(lambda x: li[x] == gabarito[x], range(len(li)))))
    print(f'Est. {nu}: {res} acertos')
    nu += 1
