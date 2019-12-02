na = int(input('Informe o número de alunos: '))

with open('binario_1.bin', 'wb') as arquivo:
    for n in range(1, na + 1):
        nome = input(f'Informe o nome do aluno {n}/{na}: ')
        nota = float(input(f'Informe a nota do aluno {n}/{na}: '))
        aluno = f'{nome} - {nota}\n'
        arquivo.write(aluno.encode('utf-8'))

with open('binario_1.bin', 'rb') as arquivo:
    lista = []
    for dado in arquivo:
        aluno = dado.decode('utf-8')
        aluno = aluno.split('-')
        aluno = {'nome': aluno[0].strip(), 'nota': float(aluno[1].strip().replace('\n', ''))}
        lista.append(aluno)
    dados = sorted(lista, key=lambda a: a['nota'], reverse=True)
    print(f"O(a) aluno(a) {dados[0]['nome']} tem a maior nota {dados[0]['nota']}")
