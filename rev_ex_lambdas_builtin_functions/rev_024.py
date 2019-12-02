from random import uniform
aluno = {}.fromkeys(['número', 'altura'], 0)
ficha = [{k: (x if k == 'número' else round(uniform(1.6, 1.9), 2)) for k, v in aluno.items()} for x in range(10)]
for c in ficha:
    print(f'{c["número"]}: {c["altura"]}m')
maior = max(ficha, key=lambda n: n['altura'])['altura']
pos_maior = max(ficha, key=lambda ma: ma['altura'])['número']
menor = min(ficha, key=lambda m: m['altura'])['altura']
pos_menor = min(ficha, key=lambda me: me['altura'])['número']
print('- ' * 5)
print(f'O maior aluno é o de cadastroa nº: {pos_maior} com {maior}m de altura')
print(f'O menor aluno é o o de cadastro nº: {pos_menor} com {menor}m de altura')
