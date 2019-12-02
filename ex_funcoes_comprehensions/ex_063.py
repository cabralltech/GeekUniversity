def compara(fr1, fr2):
    if fr1 == fr2:
        return f'"{fr1}" é igual a "{fr2}"'
    return f'"{fr1}" e "{fr2}" são diferentes'


# Programa Principal
frase1 = input('Primeira frase: ')
frase2 = input('Segunda frase:  ')
print(compara(frase1, frase2))

