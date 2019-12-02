def primo(n):
    primos = []
    for i in range(2, n):
        prime = True
        for x in range(2, i):
            if i % x == 0:
                prime = False
                break
        if prime:
            primos.append(i)
    return primos


def simplifica(num, den):
    pri_num = primo(num)
    pri_den = primo(den)
    fat_num = []
    fat_den = []
    div_1 = num
    div_2 = den
    for f in pri_num:
        while div_1 % f == 0:
            div_1 /= f
            fat_num.append(f)
    for g in pri_den:
        while div_2 % g == 0:
            div_2 /= g
            fat_den.append(g)
    menor = 0
    fat_com = {}
    for s in fat_num:
        if s in fat_den:
            if fat_num.count(s) < fat_den.count(s):
                menor = fat_num.count(s)
            else:
                menor = fat_den.count(s)
            fat_com[s] = menor
    fatoral = [key ** value for key, value in fat_com.items()]
    mdc = 1
    for j in fatoral:
        mdc *= j
    return f'{num} / {den} -› {num // mdc} / {den // mdc}'


# Programa Principal
nume = int(input('Numerador: '))
deno = int(input('Denominador: '))
print(simplifica(nume, deno))
