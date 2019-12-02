def intercalar(f1, f2):
    f1 = [x for x in f1]
    f2 = [y for y in f2]
    index = 0
    n = len(f1) + len(f2)
    for i in range(1, n, 2):
        if index < len(f2):
            f1.insert(i, f2[index])
        else:
            break
        index += 1
    return f1


# Programa Principal
frase1 = input('Escreva um palavra: ')
frase2 = input('Escreva outra palavra: ')
print(intercalar(frase1, frase2))

