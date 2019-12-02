def getchar():
    while True:
        print('- ' * 5)
        char = input('Caracter: ')
        if not char:
            print('\033[31mCaracter inexistente\033[m')
        else:
            if len(char) > 1:
                print('\033[31mDigite somente UM caracter\033[m')
            else:
                break
    return char


def rotina(vet, tamanho):
    vet = [getchar() for x in range(tamanho)]
    return f'{"- " * 15}\n{"".join(vet)}'


v = []
while True:
    try:
        tam = int(input('Tamanho do vetor: '))
        break
    except ValueError:
        print('\033[31mERRO! Valor inválido\033[m')
print(rotina(v, tam))
