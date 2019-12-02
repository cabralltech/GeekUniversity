num = int(input('Valor: '))
primo = None
if -1 <= num <= 1:
    print('ERRO! Digite um valor diferente de 0 e 1')
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
        else:
            primo = True
    if primo:
        print(f'{num} É PRIMO')
    else:
        print(f'{num} NÃO É PRIMO')
