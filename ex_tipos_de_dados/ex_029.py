media = soma = cont = 0
for i in range(1, 5):
    nota = float(input(f'{i}ª nota: '))
    soma += nota
    cont += 1
media = soma / cont
print(f'A média é {media:.1f}')
