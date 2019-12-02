def toupper(char):
    return char.upper()


while True:
    try:
        path = input('Digite um path absoluto de um arquivo texto: ')
        with open(path) as p:
            file = p.read()
            break
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m Tente novamente')
new = input('Digite o nome do novo arquivo: ')
new_file = new + '.txt'
with open(new_file, 'w') as newf:
    for i in file:
        newf.write(toupper(i))
with open(new_file) as nf:
    final = nf.read()
print(final)