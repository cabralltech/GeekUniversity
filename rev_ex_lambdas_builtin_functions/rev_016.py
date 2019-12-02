from random import uniform

vetor = [round(uniform(1, 9), 1) for x in range(5)]
while True:
    codigo = int(input('Escolha a operação:\n'
                       '[ 0 ] Sair do programa\n'
                       '[ 1 ] Imprimir o vetor\n'
                       '[ 2 ] Imprimir o vetor na ordem inversa\n'
                       'Digite a opção: '))
    print('- ' * 15)
    if codigo == 0:
        print('PROGRAMA ENCERRADO')
        break
    elif codigo == 1:
        print(vetor)
    elif codigo == 2:
        print(vetor[::-1])
    else:
        print('\033[31mERRO! Opção inválida.\033[m')
        print('- ' * 5)
    print('- ' * 15)
