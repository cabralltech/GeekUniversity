def primo(num):
    primos = []
    for i in range(2, num+1):
        prime = True
        for c in range(2, i):
            if i % c == 0:
                prime = False
                break
        if prime:
            primos.append(i)
    return primos


def mdc(den1, den2):
    prims1 = primo(den1)
    prims2 = primo(den2)
    fat1 = []
    fat2 = []
    n1 = den1
    n2 = den2
    for i in prims1:
        while n1 % i == 0:
            n1 /= i
            fat1.append(i)
    for c in prims2:
        while n2 % c == 0:
            n2 /= c
            fat2.append(c)
    fat_com = {}
    for x in fat1:
        if x in fat2:
            if fat1.count(x) < fat2.count(x):
                menor = fat1.count(x)
            else:
                menor = fat2.count(x)
            fat_com[x] = menor
    madico = 1
    fatoral = [k ** v for k, v in fat_com.items()]
    if len(fatoral) > 0:
        for ma in fatoral:
            madico *= ma
        else:
            madico = den1 * den2
    return int(madico)


def mmc(den1, den2):
    prim1 = primo(den1)
    prim2 = primo(den2)
    ft1 = []
    ft2 = []
    d1 = den1
    d2 = den2
    for i in prim1:
        while d1 % i == 0:
            d1 /= i
            ft1.append(i)
    for c in prim2:
        while d2 % c == 0:
            d2 /= c
            ft2.append(c)
    comuns = {}
    for x in ft1:
        if x in ft2:
            if ft1.count(x) > ft2.count(x):
                maior = ft1.count(x)
            else:
                maior = ft2.count(x)
            comuns[x] = maior
            if ft1.count(x) == ft2.count(x) and ft1.count(x) == 1:
                comuns[x] = 2
        else:
            comuns[x] = ft1.count(x)
    for z in ft2:
        if z not in ft1:
            comuns[z] = ft2.count(z)
    fator = [k ** v for k, v in comuns.items()]
    memuco = 1
    for me in fator:
        memuco *= me
    return int(memuco)


def simples(num, den):
    div_com = mdc(num, den)
    n = int(num / div_com)
    d = int(den / div_com)
    return n, d


def soma(f1, f2):
    den_com = mmc(f1[1], f2[1])
    num1 = int((den_com / f1[1]) * f1[0])
    num2 = int((den_com / f2[1] * f2[0]))
    soma_num = int(num1 + num2)
    f = simples(soma_num, den_com)
    return frac(f)


def sub(f1, f2):
    dc = mmc(f1[1], f2[1])
    nu1 = int((dc / f1[1]) * f1[0])
    nu2 = int((dc / f2[1]) * f2[0])
    sub_nu = int(nu1 - nu2)
    f = simples(abs(sub_nu), dc)
    if sub_nu < 0:
        return f'-{frac(f)}'
    else:
        return frac(f)


def mult(f1, f2):
    num = f1[0] * f2[0]
    den = f1[1] * f2[1]
    f = simples(num, den)
    return frac(f)


def div(f1, f2):
    num = f1[0] * f2[1]
    den = f1[1] * f2[0]
    f = simples(num, den)
    return frac(f)


def frac(f):
    return f'{f[0]}/{f[1]}'
