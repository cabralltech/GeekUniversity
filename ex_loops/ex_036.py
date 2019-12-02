quad = somaquad = soma = dif = 0
for i in range (1, 101):
    quad = i ** 2
    somaquad += quad
    soma += i
soma = soma ** 2
dif = soma - somaquad
print(f'A diferença entre a soma dos quadrados dos '
      f'cem primeiro número naturais e o quadrado '
      f'da soma é {dif}')
