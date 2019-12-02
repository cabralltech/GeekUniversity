from random import choice
mat = [[0 for x in range(10)] for y in range(5)]
answers = []
for an in range(10):
    answer = choice(['a', 'b', 'c', 'd'])
    answers.append(answer)
print('- ' * 10)
print(f'Gabarito: {answers}')
print('- ' * 10)
print('Respostas dos alunos')
for s in range(5):
    print(f'Est. {s+1}:', end=" ")
    for a in range(10):
        res = choice(['a', 'b', 'c', 'd'])
        mat[s][a] = res
        print(f'{mat[s][a]:^3}', end=' ')
    print()
result = 0
students = []
for st in range(5):
    for ans in range(10):
        if mat[st][ans] == answers[ans]:
            result += 1
    students.append(result)
    result = 0
print('- ' * 10)
for i in range(5):
    print(f'Est. {i+1}: {students[i]} acertos')
