aluno = {}
cadastro = []
maior = menor = 0.0
matma = matme = 0
for i in range(10):
    aluno['matrícula'] = int(input('Matrícula: '))
    aluno['altura'] = float(input('Altura em metros: '))
    cadastro.append(aluno.copy())
for ind, alu in enumerate(cadastro):
    if ind == 0:
        maior = menor = alu['altura']
        matma = matme = alu['matrícula']
    else:
        if alu['altura'] > maior:
            maior = alu['altura']
            matma = alu['matrícula']
        if alu['altura'] < menor:
            menor = alu['altura']
            matme = alu['matrícula']
print(f'O aluno mais alto é {matma} com {maior}m de altura\nO mais baixo é {matme} com {menor}m de altura')
