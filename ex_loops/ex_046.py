from random import randint
comp = randint(1, 10)
print('Eu pensei em um número de 1 a 10')
jog = int(input('Tente advinhar: '))
cont = 0
if comp == jog:
    print('Wow, vc acertou de primeira')
else:
    while comp != jog:
        cont += 1
        if jog > comp:
            print('Muito alto, tente novamente: ', end='')
            jog = int(input())
        elif jog < comp:
            print('Muito baixo, tente novamente: ', end='')
            jog = int(input())
    print(f'Isso! vc acertou depois de {cont} tentativa(s)')
