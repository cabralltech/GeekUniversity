def fibonacci(x):
    cont = 1
    f1 = 0
    f2 = 1
    while cont < x:
        yield f1
        f1, f2 = f2, f1 + f2
        cont += 1


for n in fibonacci(10):
    print(n, end=' ')
