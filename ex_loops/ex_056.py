primo = None
n = 21
soma = 0
for i in range(3, n):
    for c in range(2, i):
        if i % c == 0:
            primo = False
            break
        else:
            primo = True
    if primo:
        soma += i
        print(i, end=' ')
print(f'= {soma + 2}')
