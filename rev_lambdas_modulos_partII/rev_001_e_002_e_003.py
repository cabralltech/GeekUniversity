from datetime import date


def dobro(a):
    return a * 2


def data_atual(n):
    n = str(n).split('-')
    mes = ('janeiro', 'fevereiro', 'março', 'abril', 'maio',
           'junho', 'julho', 'agosto', 'setembro',
           'outubro', 'novembro', 'dezembro')
    month = int(n[1]) -1
    return f'{n[2]} de {mes[month]} de {n[0]}'


def real(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0
