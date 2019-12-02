matriz = [[0 for x in range(4)] for y in range(4)]
print(matriz)
for lin in range(4):
    for col in range(4):
        matriz[lin][col] = int(input(f'Valor [{lin}][{col}]: '))
count = 0
for lin in range(4):
    for col in range(4):
        if matriz[lin][col] > 10:
            count += 1
print(f'A matriz contém {count} valores maiores que 10')
