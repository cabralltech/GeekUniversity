from random import uniform

notas = [round(uniform(1, 10), 1) for x in range(15)]
print(notas)
print('- ' * 15)
media = sum(notas) / len(notas)
print(f'A média geral da turma é {round(media, 1)}')
