alunx = {}
notas = []
for i in range(3):
    alunx.clear()
    while True:
        try:
            alunx['mat'] = int(input('Número de matrícula: '))
            break
        except ValueError:
            print('Favor digitar somente números')
    while True:
        try:
            alunx['provas'] = float(input('Média das provas: '))
            break
        except ValueError:
            print('Nota inválida')
    while True:
        try:
            alunx['trabalhos'] = float(input('Média dos trabalhos: '))
            break
        except ValueError:
            print('Nota inválida')
    nt_final = (alunx['provas'] + alunx['trabalhos']) / 2
    alunx['nota final'] = round(nt_final, 1)
    notas.append(alunx.copy())
for i in notas:
    print(i)
maior_nota = max(notas, key=lambda a: a['nota final'])
print('- ' * 15)
print(f'A maior nota final foi a do '
      f'aluno {maior_nota["mat"]} '
      f'com a nota {maior_nota["nota final"]}')
print('- ' * 15)
media = sum(map(lambda c: c['nota final'], notas)) / len(notas)
print(f'A média aritimética das notas finais é {round(media, 1)}')
