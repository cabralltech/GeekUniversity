nome = 'Mhirley'
for v in enumerate(nome):
    print(v, end=' ')
print()
for v, l in enumerate(nome):
    if v < len(nome) - 1:
        print(f'{v}: {l}', end=' | ')
    else:
        print(f'{v}: {l}')
soma = ''
for l in nome:
    soma += l
print(soma)

num = int(input('Número de linhas: '))
for lin in range(num, 0, -1):
    print('*' * lin)

num = int(input('Número de linhas: '))
ast = ((num - 1) * 2) + 1
esp = 0
for lin in range(0, num):
    print(f'{" " * esp}{"*" * ast}')
    ast -= 2
    esp += 1

for l in range(len(nome)):
    for c in range(0, l+1):
        print(nome[c], end='')
    print()
letra = len(nome)
for l in range(len(nome)):
    for c in range(0, letra-1):
        print(nome[c], end='')
    letra -= 1
    print()

lista = list(range(100, -1, -20))
print(lista)
