def tamanho(string):
    frase = [x for x in string]
    fras = set(frase)
    return f'A palavra {string} tem {len(frase)} caracteres e {len(fras)} letras'


# Programa Principal
fra = input('Escreva uma palavra qualquer: ')
print(tamanho(fra))
