aluno = {}
turma =[]
media = media_arit = soma = 0
for i in range(5):
    aluno['matrícula'] = int(input(f'Matrícula {i+1}º aluno: '))
    aluno['média provas'] = int(input(f'Média das provas: '))
    aluno['média trabalhos'] = int(input(f'Média dos trabalhos: '))
    media = (aluno['média provas'] + aluno['média trabalhos']) / 2
    aluno['nota final'] = media
    turma.append(aluno.copy())
print('- ' * 15)
for c in turma:
    for k, v in c.items():
        print(f'{k.title()}: {v}')
    soma += c['nota final']
    print('- ' * 5)
media_arit = soma / len(turma)
print('- ' * 15)
print(f'A média da turma é {media_arit:.1f}')
