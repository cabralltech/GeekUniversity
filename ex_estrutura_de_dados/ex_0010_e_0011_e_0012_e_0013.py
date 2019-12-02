from random import randint
notas = [randint(1, 10) for nota in range(15)]
media = sum(notas) / len(notas)
print(notas)
print(f'A média geral da turma é {media:.1f}')

numeros = [randint(-9, 9) for num in range(10)]
print(numeros)
neg = pos = 0
for i in numeros:
    if i < 0:
        neg += 1
    else:
        pos += 1
print(f'A quantidade de números negativos é {neg} e a de positivos é {pos}')

nums = [randint(1, 99) for n in range(5)]
media = sum(nums) / len(nums)
print(nums)
print(f'O maior valor é {max(nums)}, o menor valor é {min(nums)} e a média é {media:.1f}')

cinco = [randint(1, 99) for c in range(5)]
print(cinco)
for num in range(len(cinco)):
    if cinco[num] == max(cinco):
        print(f'O maior valor é {cinco[num]} e ele está na posição {num}')
