def linha(n):
    print('- ' * n)


vetor = [1, 0, 5, -2, -5, 7]
# for i in range(6):
#    vetor.append(int(input('Valor: ')))
print(vetor)
soma = sum([vetor[x] for x in vetor if x == 0 or x == 1 or x == 5])
linha(5)
print(soma)
linha(5)
vetor[4] = 100
[print(n) for n in vetor]


