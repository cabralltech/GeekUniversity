n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
maior = menor = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
resp = 0
while resp != 5:
    print('- ' * 15)
    resp = int(input('Escolha:\n'
                     '[ 1 ] ADIÇÃO\n'
                     '[ 2 ] SUBTRAÇÃO\n'
                     '[ 3 ] MULTIPLICAÇÃO\n'
                     '[ 4 ] DIVISÃO\n'
                     '[ 5 ] SAIR DO PROGRAMA\n'
                     'Digite a opção: '))
    print('- ' * 15)
    if resp == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif resp == 2:
        print(f'{maior} - {menor} = {maior - menor}')
    elif resp == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif resp == 4:
        print(f'{maior} / {menor} = {maior / menor:.1f}')
print('- ' * 15)
print('PROGRAMA ENCERRADO')