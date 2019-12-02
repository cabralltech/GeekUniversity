def primo(x):
    prime = True
    if len([y for y in range(2, x+1) if x % y == 0]) > 1:
        prime = False
    return prime


def fatoral(x):
    prims = [a for a in range(2, x+1) if primo(a)]
    fat = [b for b in prims if x % b == 0]
    return fat


def simplifica(n, d):
    mdn = {}
    mdd = {}
    nu = n
    de = d
    for i in fatoral(n):
        cont = 0
        while nu % i == 0:
            nu /= i
            cont += 1
        mdn[i] = cont
    for v in fatoral(d):
        con = 0
        while de % v == 0:
            de /= v
            con += 1
        mdd[v] = con
    mdc = 1
    for k in mdn.keys():
        if k in mdd.keys():
            mdc *= k ** min(mdn[k], mdd[k])
    nume = int(n // mdc)
    deno = int(d // mdc)
    return f'A fração {n}/{d} simplificada é {nume}/{deno}'


while True:
    try:
        num = int(input('Numerador: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
while True:
    try:
        den = int(input('Denominador: '))
        if den == 0:
            print('\033[31mERRO! Não existe divisão por 0\033[m')
        else:
            break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(simplifica(num, den))
