def primo(n):
    prime = True
    if len([a for a in range(2, n+1) if n % a == 0]) > 1:
        prime = False
    return prime


def primos(n):
    prims = [b for b in range(2, n+1) if primo(b)]
    return prims


def fatoral(n):
    fat = [c for c in primos(n) if n % c == 0]
    return fat


def mdc(x, y):
    madx = {}
    mady = {}
    for i in fatoral(x):
        cont = 0
        while x % i == 0:
            x /= i
            cont += 1
        madx[i] = cont
    for t in fatoral(y):
        conta = 0
        while y % t == 0:
            y /= t
            conta += 1
        mady[t] = conta
    prod = 1
    for k in madx.keys():
        if k in mady.keys():
            prod *= k ** min(madx[k], mady[k])
    return prod


def mmc(xis, yps):
    micx = {}
    micy = {}
    for r in fatoral(xis):
        co = 0
        while xis % r == 0:
            xis /= r
            co += 1
        micx[r] = co
    for u in fatoral(yps):
        con = 0
        while yps % u == 0:
            yps /= u
            con += 1
        micy[u] = con
    pro = 1
    for ki in micx.keys():
        if ki in micy.keys():
            pro *= ki ** max(micx[ki], micy[ki])
        else:
            pro *= ki ** micx[ki]
    for kl in micy.keys():
        if kl not in micx.keys():
            pro *= kl ** micy[kl]
    return pro


def soma(f1, f2):
    mic = mmc(f1[1], f2[1])
    som = int((mic / f1[1]) * f1[0]) + int((mic / f2[1]) * f2[0])
    return simplifica(som, mic)


def sub(f1, f2):
    mic = mmc(f1[1], f2[1])
    subtr = int((mic / f1[1] * f1[0]) - int((mic / f2[1]) * f2[0]))
    return simplifica(subtr, mic)


def mult(f1, f2):
    numer = f1[0] * f2[0]
    denom = f1[1] * f2[1]
    return simplifica(numer, denom)


def div(f1, f2):
    numera = f1[0] * f2[1]
    denom = f1[1] * f2[0]
    return simplifica(numera, denom)


def simplifica(n, d):
    div = mdc(n, d)
    if d >= div <= n:
        num = n // div
        den = d // div
        return num, den
    return n, d


# Programa Principal
print('- ' * 15)
print(f'{"PRIMEIRA FRAÇÃO"}')
print('- ' * 15)
while True:
    try:
        numerador1 = int(input('Numerador: '))
        break
    except ValueError:
        print('\033[31mValor iválido\033[m')
while True:
    try:
        denominador1 = int(input('Denominador: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
print(f'{numerador1}/{denominador1} -›', end=' ')
fra1 = simplifica(numerador1, denominador1)
print(f'{fra1[0]}/{fra1[1]}')
print('- ' * 15)
print(f'{"SEGUNDA FRAÇÃO"}')
print('- ' * 15)
while True:
    try:
        numerador2 = int(input('Numerador: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
while True:
    try:
        denominador2 = int(input('Denominador: '))
        break
    except ValueError:
        print('\033[31mValor inválido\033[m')
print(f'{numerador2}/{denominador2} -›', end=' ')
fra2 = simplifica(numerador2, denominador2)
print(f'{fra2[0]}/{fra2[1]}')
print('- ' * 15)
adicao = soma(fra1, fra2)
print(f'{fra1[0]}/{fra1[1]} + {fra2[0]}/{fra2[1]} = {adicao[0]}/{adicao[1]}')
subt = sub(fra1, fra2)
print(f'{fra1[0]}/{fra1[1]} - {fra2[0]}/{fra2[1]} = {subt[0]}/{subt[1]}')
mul = mult(fra1, fra2)
print(f'{fra1[0]}/{fra1[1]} x {fra2[0]}/{fra2[1]} = {mul[0]}/{mul[1]}')
divi = div(fra1, fra2)
print(f'{fra1[0]}/{fra1[1]} / {fra2[0]}/{fra2[1]} = {divi[0]}/{divi[1]}')
