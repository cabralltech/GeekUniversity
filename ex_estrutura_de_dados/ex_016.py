def sit(a):
    if a < 5.0:
        return 'REPROVADO'
    elif a < 7.0:
        return 'RECUPERAÇÃO'
    else:
        return 'APROVADO'


# Programa Principal
from random import choice
gabarito = [choice(['a', 'b', 'c', 'c']) for x in range(10)]
aluno = {}
turma = []
for i in range(3):
    aluno['matrícula'] = int(input('Número de matrícula: '))
    respostas = [choice(['a', 'b', 'c', 'c']) for x in range(10)]
    aluno['respostas'] = respostas[:]
    cont = 0
    for c in range(len(gabarito)):
        if gabarito[c] == respostas[c]:
            cont += 1
    aluno['nota'] = cont
    aluno['situação'] = sit(cont)
    turma.append(aluno.copy())
    respostas.clear()
print('- ' * 15)
for alu in turma:
    for k, v in alu.items():
        print(f'{k.title()}: {v}')
    print('- ' * 5)