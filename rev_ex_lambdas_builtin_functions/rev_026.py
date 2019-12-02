from random import randint
vetor = [randint(1, 20) for x in range(10)]
media = sum(vetor) / len(vetor)
somatorio = sum([(vetor[n] - media) ** 2 for n in range(len(vetor))])
desvio = (somatorio / (len(vetor) - 1)) ** 0.5
print(vetor)
print('- ' * 15)
print(f'O desvio padrão do vetor acima é {desvio:.2f}')
