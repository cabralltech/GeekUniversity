def concatena(str1, str2, n):
    return f'{str1} {str2[:n]} NULL'


# Programa Principal
frase1 = input('Primeira palavra: ')
frase2 = input('Segunda palavra: ')
letras = int(input('Número de letras da segunda palavra: '))
print(concatena(frase1, frase2, letras))
