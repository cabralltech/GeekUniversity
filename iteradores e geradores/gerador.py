def conta_ate(num_max):
    cont = 1
    while cont <= num_max:
        yield cont
        cont += 1


for i in conta_ate(5):
    print(i)
