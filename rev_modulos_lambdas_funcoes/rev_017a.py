from random import randint
mat = [[randint(4, 9) for x in range(3)] for y in range(10)]
for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(mat[l][c], end=' ')
    print()
print('- ' * 15)
provas = list(map(lambda a: a.index(min(a)), mat))
print(provas)
# for li in mat:
#     provas.append(li.index(min(li)))
pr_1 = provas.count(0)
pr_2 = provas.count(1)
pr_3 = provas.count(2)
print(f'A quantidade de alunxs que a pior nota foi na 1ª prova é {pr_1}')
print(f'A quantidade de alunxs que a pior nota foi na 2ª prova é {pr_2}')
print(f'A quantidade de alunxs que a pior nota foi na 3ª prova é {pr_3}')
