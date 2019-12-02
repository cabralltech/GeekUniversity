n = int(input('Digite o valor de n: '))
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))
c = x = 0
while c < n:
    if x % i == 0 or x % j == 0:
        print(x, end=' ')
        c += 1
    x += 1

