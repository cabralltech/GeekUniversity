def cos_taylor(ang):
    pi = 3.141593
    rad = ang * pi / 180
    fat = []
    for i in range(10):
        f = 1
        if i >= 1:
            for c in range(1, i):
                f *= c
            fat.append(f)
    taylor = [(rad ** x) / fat[x] for x in range(10) if x % 2 == 0]
    soma = sub = 0
    for co in range(len(taylor)):
        if co % 2 == 0:
            soma += taylor[co]
        else:
            sub += taylor[co]
    return f'Série de Taylor cosseno de {ang}°\n{taylor}\nCosseno = {soma - sub:.2f}'


# Programa Principal
angulo = float(input('Ângulo: '))
print(cos_taylor(angulo))
