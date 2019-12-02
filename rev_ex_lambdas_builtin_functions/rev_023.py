from random import uniform
conj1 = [round(uniform(0, 9), 1) for x in range(5)]
conj2 = [round(uniform(0, 9), 1) for y in range(5)]
produto = sum(conj1[n] * conj2[n] for n in range(5))
print(conj1)
print('- ' * 15)
print(conj2)
print('- ' * 15)
print(f'O produto escalar dos vetores acima é {produto}')
