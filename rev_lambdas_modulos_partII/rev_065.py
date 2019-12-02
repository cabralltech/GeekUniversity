def null(st1, st2, n):
    return st2[:n]+' '+st1+' '+'NULL'


while True:
    frase1 = input('1ª frase: ')
    if len(frase1) < 2:
        print('\033[31mFavor digitar, pelo menos, duas palavras\033[m')
    else:
        break
while True:
    frase2 = input('2ª frase: ')
    if len(frase2) < 2:
        print('\033[31mFavor digitar, pelo menos, duas palavras\033[m')
    else:
        break
while True:
    try:
        num = int(input('Número de letras: '))
        break
    except ValueError:
        print('\033[31mERRO! Somente números\033[m')
print('- ' * 15)
print(null(frase1, frase2, num))