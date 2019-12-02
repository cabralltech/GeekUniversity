def primo(n):
    prime = True
    if len([x for x in range(2, n+1) if n % x == 0]) > 1:
        prime = False
    return prime


def primos(n):
    prims = [y for y in range(2, n+1) if primo(y)]
    return prims


def fator(n):
    fat = [z for z in primos(n) if n % z == 0]
    return fat


def mdc(a, b):
    mada = {}
    madb = {}
    ax = a
    bx = b
    for i in fator(a):
        cont = 0
        while ax % i == 0:
            ax /= i
            cont += 1
        mada[i] = cont
    for j in fator(b):
        con = 0
        while bx % j == 0:
            bx /= j
            con += 1
        madb[j] = con
    mad = 1
    for k in mada.keys():
        if k in madb.keys():
            mad *= k ** min(mada[k], madb[k])
    return mad


def mmc(a, b):
    mica = {}
    micb = {}
    ay = a
    by = b
    for q in fator(a):
        co = 0
        while ay % q == 0:
            ay /= q
            co +=1
        mica[q] = co
    for w in fator(b):
        cot = 0
        while by % w == 0:
            by /= w
            cot += 1
        micb[w] = cot
    mic = 1
    for ki in mica.keys():
        if ki in micb.keys():
            mic *= ki ** max(mica[ki], micb[ki])
        else:
            mic *= ki ** mica[ki]
    for kl in micb.keys():
        if kl not in mica.keys():
            mic *= kl ** micb[kl]
    return mic


def reduz(num, den):
    div = mdc(num, den)
    if den >= div <= num:
        nu = int(num // div)
        de = int(den // div)
        return nu, de
    return num, den


def soma(f1, f2):
    dic = mmc(f1[1], f2[1])
    s = int((dic / f1[1]) * f1[0]) + int((dic / f2[1]) * f2[0])
    return s, dic


def mult(f1, f2):
    nume = f1[0] * f2[0]
    deno = f1[1] * f2[1]
    return reduz(nume, deno)


def div(f1, f2):
    numer = f1[0] * f2[1]
    denom = f1[1] * f2[0]
    return reduz(numer, denom)


while True:
    try:
        p = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        q = int(input('Valor: '))
        if q == 0:
            raise ZeroDivisionError
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
    except ZeroDivisionError:
        print('\033[31mERRO! não existe divisão por 0\033[m')
print(f'Fração: {p}/{q}')
print('- ' * 5)
print(f'Simplificada: {reduz(p, q)[0]}/{reduz(p, q)[1]}')
print(f'Negativo: - {reduz(p, q)[0]}/{reduz(p, q)[1]}')
print('- ' * 5)
while True:
    try:
        pa = int(input('Valor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        qa = int(input('Valor: '))
        if qa == 0:
            raise ZeroDivisionError
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
    except ZeroDivisionError:
        print('\033[31mERRO! Não existe divisão por 0\033[m')
print(f'Fração: {pa}/{qa}')
fra1 = reduz(p, q)
fra2 = reduz(pa, qa)
print('- ' * 5)
print(f'Simplificada: {reduz(pa, qa)[0]}/{reduz(pa, qa)[1]}')
print(f'Negativo: - {reduz(pa, qa)[0]}/{reduz(pa, qa)[1]}')
print('- ' * 5)
print(f'{fra1[0]}/{fra1[1]} + {fra2[0]}/{fra2[1]} = {soma(fra1, fra2)[0]}/{soma(fra1, fra2)[1]}')
print(f'{fra1[0]}/{fra1[1]} x {fra2[0]}/{fra2[1]} = {mult(fra1, fra2)[0]}/{mult(fra1, fra2)[1]}')
print(f'{fra1[0]}/{fra1[1]} / {fra2[0]}/{fra2[1]} = {div(fra1, fra2)[0]}/{div(fra1, fra2)[1]}')
