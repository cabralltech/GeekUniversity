from random import uniform
vet = [round(uniform(1, 9), 1) for x in range(11)]
print(vet)
print(max(vet))
sort1 = sorted([max(vet) if a == 5 else vet[a] for a in range(6)])
sort2 = sorted([vet[b] for b in range(6, 11)], reverse=True)
sort3 = sort1 + sort2
print(sort3)
