from random import randint
a = randint(1000, 9999)
b = randint(1000, 9999)
veta = [a // (10 ** x) % 10 for x in range(len(str(a)))]
vetb = [b // (10 ** n) % 10 for n in range(len(str(b)))]
print(f'{a} -› {veta}')
print(f'{b} -› {vetb}')
vetc = [veta[y] + vetb[y] for y in range(len(veta))]
print('- ' * 10)
print('Soma dos vetores acima')
print(vetc)
