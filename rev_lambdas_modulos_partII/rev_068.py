def intercalar(st1, st2):
    st3 = []
    c = 0
    for i in range(len(st1)):
        st3.append(st1[i])
        if i < len(st2):
            st3.append(st2[i])
    return st3


while True:
    pal1 = input('1ª palavra: ')
    if not pal1:
        print('\033[31mERRO! Palavra não detectada\033[m')
    else:
        break
while True:
    pal2 = input('2ª palavra: ')
    if not pal2:
        print('\033[31mERRO! Palavra não detectada\033[m')
    else:
        break
print(intercalar(pal1, pal2))