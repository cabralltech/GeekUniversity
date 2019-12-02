c = 0
vet = []
while c < 10:
    n = int(input('Valor: '))
    if n not in vet:
        vet.append(n)
        c += 1
    else:
        print('Valor já adicionado, tente outra vez.')
print('- ' * 15)
print(vet)
