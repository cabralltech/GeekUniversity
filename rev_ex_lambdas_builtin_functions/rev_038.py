vet = []
for i in range(5):
    n = int(input('Valor: '))
    if i == 0 or n > vet[-1]:
        vet.append(n)
    else:
        k = 0
        while k < len(vet):
            if n <= vet[k]:
                vet.insert(k, n)
                break
            k += 1
print(vet)
