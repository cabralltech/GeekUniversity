soma = 0
f1 = 0
f2 = 1
while soma < 4_000_000:
    fb = f1 + f2
    f1 = f2
    f2 = fb
    if fb % 2 ==0:
        soma += fb
        print(fb, end=' ')
print()
print('- ' * 15)
print(f'A soma dos pares de Fibonacci, menor que 4mi é {soma}')
