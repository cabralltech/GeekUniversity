def sen_taylor(ang):
    pi = 3.141593
    rad = ang * pi / 180
    fat = []
    for i in range(11):
        f = 1
        if i > 1:
            for x in range(1, i+1):
                f *= x
        fat.append(f)
    taylor = [(rad ** x) / fat[x] for x in range(11) if x > 1 and x % 2 != 0]
    taylor.insert(0, rad)
    soma = sub = 0
    for c in range(len(taylor)):
        if c % 2 == 0:
            soma += taylor[c]
        else:
            sub += taylor[c]
    return f'Série de Taylor do ângulo de {ang}°:\n{taylor}\nSeno = {soma - sub:.2f}'


# Programa Principal
angulo = float(input('Valor ângulo: '))
print(sen_taylor(angulo))
