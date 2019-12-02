idade = 1
soma = media = cont = 0
while idade > 0:
    cont += 1
    idade = int(input('Idade: '))
    soma += idade
media = soma / (cont - 1)
print(f'A média das idades cadastradas é {media:.1f}')
