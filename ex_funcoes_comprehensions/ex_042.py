from random import uniform
def media(n):
    soma = media = 0
    for i in n:
        soma += i
    media = soma / len(n)
    return f'Lista de números:\n{n}\n{"- " * 10}\nA média da lista acima é {media:.2f}'


# Programa Principal
num = [round(uniform(1, 9), 2) for x in range(10)]
print(media(num))
