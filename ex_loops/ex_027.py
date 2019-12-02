num = int(input('Valor: '))
harm = 1
for i in range(2, num+1):
    harm += 1/i
print(f'H({num}) = {harm:.1f}')

