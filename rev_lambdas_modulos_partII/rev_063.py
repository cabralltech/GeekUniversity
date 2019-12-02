def compara(st1, st2):
    if st1 == st2:
        return 'As frases são iguais'
    return 'As frases são diferentes'


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
print(compara(frase1, frase2))
