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
        con = 0
        while y % t == 0:
            y /= t
            con += 1
        mady[t] = con
    prod = 1
    for k in madx.keys():
        if k in mady.keys():
            prod *= k ** min(madx[k], mady[k])
    print(madx)
    print(mady)
    print(prod)


numerador = int(input('Numerador: '))
denominador = int(input('Denominador: '))
print(mdc(numerador, denominador))
