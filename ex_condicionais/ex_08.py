nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = 0
if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
    print('Nota inválida')
else:
    media = (nota1 + nota2) / 2
    print(f'A media do aluno é {media:.1f}')
