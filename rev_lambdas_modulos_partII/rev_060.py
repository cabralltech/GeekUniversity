def primeira_letra(frase, pal):
    if pal in frase:
        return f'A primeira letra de {pal} é "{pal[0]}"'
    return -1


while True:
    frase = input('Digite uma frase: ')
    fra = frase.split(' ')
    if len(fra) < 2:
        print('\033[31mFavor digitar, pelo menos duas palavras\033[m')
    else:
        break
print('- ' * 15)
print(frase)
print('- ' * 15)
while True:
    pal = input('Escolha uma palavra dentro da frase acima: ')
    if pal:
        break
    else:
        print('\033[31mFavor digitar uma palavra\033[m')
        print('- ' * 5)
print('- ' * 5)
print(primeira_letra(fra, pal))

