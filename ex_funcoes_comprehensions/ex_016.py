def desenha_linha(num, simb):
    return simb * num


# Programa Principal
sim = input('Símbolo da linha: ')
tam = int(input('Tamanho da linha: '))
print(desenha_linha(tam, sim))
