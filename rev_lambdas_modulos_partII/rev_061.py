def anagrama(p1, p2):
    ana = [True for x in p1 if x in p2]
    if all(ana) and len(ana) == len(p1) == len(p2):
        return True
    return False


print('- ' * 15)
print(f'{"DETECTOR DE ANAGRAMAS":^30}')
print('- ' * 15)
while True:
    pal1 = input('1ª palavra: ')
    if not pal1:
        print('Favor digitar pelo menos uma palavra')
    else:
        break
while True:
    pal2 = input('2ª palavra: ')
    if not pal2:
        print('Favor digitar pelo menos uma palavra')
    else:
        break
print('- ' * 15)
print(anagrama(pal1, pal2))
