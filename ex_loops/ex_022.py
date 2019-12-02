media = cont = soma = 0
erro = False
while True:
    nota = float(input('Nota: '))
    if not 10 <= nota <= 20:
        erro = True
        break
    else:
        soma += nota
        cont += 1
if cont == 0 and erro:
    print('Nota inválida')
else:
    media = soma / cont
    print(f'A média aritimética das notas cadastadas é {media:.1f}')
