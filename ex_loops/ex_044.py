num = int(input('Valor: '))
f1 = fb = 0
f2 = 1
if num == 0:
    print(f'{f1} | {f2}')
else:
    if num > 0:
        print(f'{f1} | {f2}', end=' | ')
        for i in range(1, num-1):
            fb = f1 + f2
            f1 = f2
            f2 = fb
            if fb < num:
                print(f'{fb}', end=' | ')
            else:
                print(f'{fb}')
                break
