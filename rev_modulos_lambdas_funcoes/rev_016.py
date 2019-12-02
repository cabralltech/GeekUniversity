from random import choice
answer = ['a', 'b', 'c', 'd', 'e']
gaba = [choice(answer) for x in range(10)]
cont = 0
aluno = {}
notas = []
while cont < 3:
    aluno.clear()
    aluno['mat'] = int(input('Número de matrícula: '))
    resp = [choice(answer) for a in range(10)]
    aluno['respostas'] = resp
    aluno['nota'] = len(list(filter(lambda x: resp[x] == gaba[x], range(len(resp)))))
    notas.append(aluno.copy())
    cont += 1
print('Gabarito: ', end='   ')
for c in gaba:
    print(c, end=' ')
print()
for k in aluno.keys():
    print(f'{k.upper():<35}', end='')
print()
for al in notas:
    for v in al.values():
        print(f'{v}', end=' ' * 10)
    print()
