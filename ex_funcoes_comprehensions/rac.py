def primo(n):
    primos = []
    for i in range(2, n+1):
        prime = True
        for c in range(2, i):
            if i % c == 0:
                prime = False
                break
        if prime:
            primos.append(i)
    return primos


def frac(nu, de):
    return f'{nu}/{de}'


def neg(fra):
    return f'-{fra[0]}/{fra[1]}'


def simples(nu, de):
    dc = mdc(nu, de)
    if dc <= nu and dc <= de:
        n = nu // dc
        d = de // dc
        return n, d
    else:
        return nu, de


def mdc(d1, d2):
    fa1 = fat(d1)
    fa2 = fat(d2)
    fat_com = {}
    for f in fa1:
        if f in fa2:
            if fa1.count(f) < fa2.count(f):
                menor = fa1.count(f)
            else:
                menor = fa2.count(f)
            fat_com[f] = menor
    madico = 1
    fatoral = [k ** v for k, v in fat_com.items()]
    if len(fatoral) != 0:
        for fa in fatoral:
            madico *= fa
    else:
        madico = d1 * d2
    return int(madico)


def mmc(da, db):
    fata = fat(da)
    fatb = fat(db)
    facm = {}
    for g in fata:
        if g in fatb:
            if fata.count(g) > fatb.count(g):
                maior = fata.count(g)
                facm[g] = maior
            else:
                maior = fatb.count(g)
                facm[g] = maior
        else:
            facm[g] = fata.count(g)
    for h in fatb:
        if h not in fata:
            facm[h] = fatb.count(h)
    fator = [key ** value for key, value in facm.items()]
    mimuco = 1
    for j in fator:
        mimuco *= j
    return int(mimuco)


def fat(nume):
    pri = primo(nume)
    fa = []
    a = nume
    for p in pri:
        while a % p == 0:
            a /= p
            fa.append(p)
    return fa


def soma(f1, f2):
    n1 = simples(f1[0], f1[1])
    n2 = simples(f2[0], f2[1])
    me_mu = mmc(n1[1], n2[1])
    nu1 = (me_mu // n1[1]) * n1[0]
    nu2 = (me_mu // n2[1]) * n2[0]
    soma_nu = nu1 + nu2
    tot = soma_nu, me_mu
    return frac(tot[0], tot[1])


def mult(f1, f2):
    n1 = simples(f1[0], f1[1])
    n2 = simples(f2[0], f2[1])
    nu = n1[0] * n2[0]
    de = n1[1] * n2[1]
    tot = simples(nu, de)
    return frac(tot[0], tot[1])


def divide(f1, f2):
    n1 = simples(f1[0], f1[1])
    n2 = simples(f2[0], f2[1])
    nu = n1[0] * n2[1]
    de = n1[1] * n2[0]
    tot = simples(nu, de)
    return frac(tot[0], tot[1])