nota = float(input('Nota: '))
faltas = int(input('Número de faltas: '))
con = ' '
if faltas < 20:
    if nota >= 9:
        con = 'A'
    elif 9 > nota >= 7.5:
        con = 'B'
    elif 7.5 > nota >= 5:
        con = 'C'
    elif 5 > nota >= 4:
        con = 'D'
    else:
        con = 'E'
else:
    if nota >= 9:
        con = 'B'
    elif 9 > nota >= 7.5:
        con = 'C'
    elif 7.5 > nota >= 5:
        con = 'D'
    else:
        con = 'E'
print(f'O aluno de nota {nota} teve {faltas} faltas, é um aluno conceito {con}')
