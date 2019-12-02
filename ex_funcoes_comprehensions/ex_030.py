def cosh_taylor(ang):
    pi = 3.141493
    rad = ang * pi / 180
    fat = []
    for i in range(11):
        f = 1
        if i > 1:
            for c in range(1, i):
                f *= c
        if i > 0:
            fat.append(f)
    taylor = [(rad ** x) / fat[x] for x in range(len(fat)) if x % 2 == 0]
    soma = 0
    for cos in taylor:
        soma += cos
    return f'A série de Taylor para cosseno de {ang}°:\n{taylor}\n' \
        f'Cosseno hiperbólico na varicão de 0 a 5: {soma:.2f}'


# Programa Principal
angulo = float(input('Ângulo: '))
print(cosh_taylor(angulo))
