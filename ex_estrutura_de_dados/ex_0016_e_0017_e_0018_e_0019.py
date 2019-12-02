from random import randint
vet = [randint(1, 99) for x in range(5)]
opt = int(input('Escolha a operação:\n'
                '[ 0 ] SAIR\n'
                '[ 1 ] IMPRIMIR VETOR\n'
                '[ 2 ] IMPRIMIR VETOR INVERTIDO\n'
                'Digite a opção desejada: '))
print('- ' * 10)
if opt == 0:
    print('PROGRAMA ENCERRADO')
elif opt == 1:
    print(vet)
elif opt == 2:
    print(vet[::-1])
else:
    print('OPÇÃO INVÁLIDA')

print('= ' * 10)
vet1 = [randint(-10, 10) for y in range(10)]
print(vet1)
vet2 = [0 if z < 0 else z for z in vet1]
print(vet2)

print('= ' * 10)
vet3 = [randint(1, 99) for a in range(10)]
print(vet3)
num = int(input('Valor de 1 a 9: '))
vet4 = [b for b in vet3 if b % num == 0]
print(set(vet4))

print('= ' * 10)
vet5 = [(c + (5 * c)) % (c + 1) for c in range(50)]
print(vet5)
