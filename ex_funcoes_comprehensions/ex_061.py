def anagrama(frase1, frase2):
    f1 = {x for x in frase1}
    f2 = {y for y in frase2}
    return f1 == f2


# Programa Principal
pal1 = input('Primeira palavra: ').lower()
pal2 = input('Segunda palvra: ').lower()
print(anagrama(pal1, pal2))
