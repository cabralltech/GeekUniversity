from random import randint
v1 = [randint(1, 20) for x in range(5)]
v2 = [randint(1, 20) for y in range(5)]
print(v1)
print('- ' * 15)
print(v2)
print('- ' * 15)
v3 = [v1[n] + v2[n] for n in range(5)]
print(f'A soma dos vetores é:\n{v3}')
print('- ' * 15)
v4 = [v1[a] - v2[a] for a in range(5)]
print(f'A diferença entre os vetores é:\n{v4}')
print('- ' * 15)
v5 = [v1[b] * v2[b] for b in range(5)]
print(f'O produto dos vetores é:\n{v5}')
print('- ' * 15)
v6 = [v1[c] // v2[c] for c in range(5)]
print(f'O quociente inteiro dos vetores é:\n{v6}')
vet1 = set(v1)
vet2 = set(v2)
print('- ' * 15)
print(f'A intesecção dos vetores é:\n{vet1 & vet2}')
print('- ' * 15)
print(f'A união dos vetores é:\n{vet1 | vet2}')
