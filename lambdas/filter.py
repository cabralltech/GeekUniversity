from random import uniform
from statistics import mean

dados = [round(uniform(0, 9), 1) for x in range(10)]
media = round(mean(dados), 2)
print(dados)
print('- ' * 15)
print(f'A média do vetor acima é {media}')
acima = list(filter(lambda d: d > media, dados))
print(acima)
