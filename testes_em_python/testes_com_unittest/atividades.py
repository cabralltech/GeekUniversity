def comer(comida, saudavel=True):
    junk = [
        'pizza',
        'sorvete',
        'hamburguer',
        'cachorro-quente',
        'doces'
    ]
    if comida in junk:
        saudavel, msg = False, 'viver intensamente'
    else:
        msg = 'uma vida saudável'
    return f'Eu como {comida} porque gosto de {msg}'


def dormir(horas=8, cansada=False):
    if horas < 8:
        cansada, msg = True, 'cansada o tempo inteiro'
    else:
        msg = 'bem por isso'
    return f'Eu durmo {horas} por noite e me sinto {msg}'

