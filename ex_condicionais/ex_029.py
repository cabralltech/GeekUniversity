from random import randint
res = False
correto = []
for i in range(1, 6):
    a = randint(1, 100)
    b = randint(1, 100)
    aluno = int(input(f'Qual é a soma de {a} + {b}? '))
    if aluno == a + b:
        res = True
        correto.append(aluno)
print(f'Você acertou {len(correto)} vez(es), as respostas corretas foram: {correto}')
