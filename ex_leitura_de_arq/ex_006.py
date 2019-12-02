from collections import Counter


def counter_alfabeto(file):
    alf = 'abcdefghijklmnopqrstuwvxyz'
    fil = [x for x in file.lower() if x in alf]
    return Counter(fil)


def count_alfa(file):
    alf = 'abcdefghijklmnopqrstuwvxyz'
    return {x: file.count(x) for x in file if x in alf}


while True:
    try:
        path = input('Digite um path absoluto: ')
        with open(path) as p:
            arq = p.read().lower()
            break
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m Tente novamente')
print('- ' * 15)
print(counter_alfabeto(arq))
print('- ' * 15)
print(count_alfa(arq))
