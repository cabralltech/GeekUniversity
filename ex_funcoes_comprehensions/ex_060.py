def encontrar(string):
    sub_string = input('Parte a ser encontrada: ').strip()
    string.split(' ')
    if sub_string in string:
        return f'A primeira letra da palavra "{sub_string}" é "{sub_string[0]}"'
    return -1


# Programa Principal
frase = input('Ecreva uma frase:')
print(encontrar(frase))
