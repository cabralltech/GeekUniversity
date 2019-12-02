def uni(a):
    if a == '1':
        return 'um'
    elif a == '2':
        return 'dois'
    elif a == '3':
        return 'três'
    elif a == '4':
        return 'quatro'
    elif a == '5':
        return 'cinco'
    elif a == '6':
        return 'seis'
    elif a == '7':
        return 'sete'
    elif a == '8':
        return 'oito'
    elif a == '9':
        return 'nove'


def teens(a):
    if a == '10':
        return 'dez'
    elif a == '11':
        return 'onze'
    elif a == '12':
        return 'doze'
    elif a == '13':
        return 'treze'
    elif a == '14':
        return 'catorze'
    elif a == '15':
        return 'quinze'
    elif a == '16':
        return 'dezesseis'
    elif a == '17':
        return 'dezessete'
    elif a == '18':
        return 'dezoito'
    elif a == '19':
        return 'dezenove'


def dez0(a):
    if a[0] == '2':
        return 'vinte'
    elif a[0] == '3':
        return 'trinta'
    elif a[0] == '4':
        return'quarenta'
    elif a[0] == '5':
        return 'cinquenta'
    elif a[0] == '6':
        return 'sessenta'
    elif a[0] == '7':
        return 'setenta'
    elif a[0] == '8':
        return 'oitenta'
    elif a[0] == '9':
        return 'noventa'


def dez(a):
    if a[1] == '0':
        return dez0(a)
    else:
        return dez0(a) + 'e' + uni(a[1])


def cen0(a):
    if a[0] == '1':
        return 'cem'
    elif a[0] == '2':
        return 'duzentos'
    elif a[0] == '3':
        return 'trezentos'
    elif a[0] == '4':
        return 'quatrocentos'
    elif a[0] == '5':
        return 'quinhentos'
    elif a[0] == '6':
        return 'seiscentos'
    elif a[0] == '7':
        return 'setecentos'
    elif a[0] == '8':
        return 'oitocentos'
    elif a[0] == '9':
        return 'novecentos'


def cen1(a):
    if a[0] == '1':
        if a[1] == '0':
            return 'centoe' + uni(a[2])
        elif a[1] == '1':
            return 'centoe' + teens(a[1:])
        else:
            return 'centoe' + dez(a[1:])
    else:
        if a[1] == '0':
            return cen0(a) + 'e' + uni(a[2])
        elif a[1] == '1':
            return cen0(a) + 'e' + teens(a[1:])
        else:
            return cen0(a) + 'e' + dez(a[1:])


def cen(a):
    if a[1:] == '00':
        return cen0(a)
    else:
        return cen1(a)


# Programa Principal
somauni = somateens = somadez = somacem = soma = 0
for i in range(1, 1000):
    num = str(i)
    if len(num) < 2:
        num = uni(num)
        somauni += len(num)
    elif len(num) < 3:
        if num[0] == '1':
            num = teens(num)
            somateens += len(num)
        else:
            num = dez(num)
            somadez += len(num)
    elif len(num) == 3:
        num = cen(num)
        somacem += (len(num))
soma = somauni + somateens + somadez + somacem
print(f'A soma de todas as letras de 1 a 1000 é {soma}')
