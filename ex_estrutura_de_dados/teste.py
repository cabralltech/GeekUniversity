from random import choice
gabarito = [choice(['a', 'b', 'c', 'c']) for x in range(10)]
respostas = [choice(['a', 'b', 'c', 'c']) for x in range(10)]
for c in range(len(gabarito)):
    print(gabarito[c], end=' - ')
    print(respostas[c])
cont = 0
for i in range(len(gabarito)):
    if gabarito[i] == respostas[i]:
        cont += 1
print(cont)

num = input('Valor: ')
if int(num) > 0:
    nu = [int(n) for n in num]
    print(nu)
