from random import randint
res = [[0 for x in range(3)] for y in range(5)]
for alu in range(5):
    for no in range(3):
        res[alu][no] = randint(1, 10)
prova1 = prova2 = prova3 = 0
for a in range(5):
    if res[a][0] < 5:
        prova1 += 1
print(f'{prova1} alunx(s) tiraram nota(s) abaixo de 5.0')
for a in range(5):
    if res[a][1] < 5:
        prova2 += 2
print(f'{prova2} alunx(s) tiraram nota(s) abaixo de 5.0')
for a in range(5):
    if res[a][2] < 5:
        prova3 += 1
print(f'{prova3} alunx(s) tiraram nota(s) abaixo de 5.0')
