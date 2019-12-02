import time

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio


lis_inicio = time.time()
print(sum([n for n in range(100000000)]))
lis_tempo = time.time() - lis_inicio

print('- ' * 15)
print(gen_tempo, 'X', lis_tempo)
