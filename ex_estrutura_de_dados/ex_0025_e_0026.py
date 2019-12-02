from random import randint

vet = [num for num in range(101) if num % 7 == 0 or num // 1 % 10 == 7]
print(vet)

vetor = [randint(1, 9) for x in range(5)]
print(vetor)
media = sum(vetor) / len(vetor)
somatorio = [(num - media) ** 2 for num in vetor]
print(somatorio)
soma = sum(somatorio)
print(soma)
var = soma / (len(vetor) - 1)
print(var)
desvio = var ** 0.5
print(f'O desvio padrão do vetor acima é {desvio:.1f}')
