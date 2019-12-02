notas = []
soma = 0
for i in range(0, 3):
    n = float(input(f'{i + 1}ª nota: '))
    soma += n
    notas.append(n)
soma += notas[2]
media = soma / 4
if media > 6.0:
    print(f'APROVADO com média {media:.1f}')
else:
    print(f'REPROVADO com média {media:.1f}')
