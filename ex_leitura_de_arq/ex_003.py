while True:
    try:
        arq = input('Digite o path absoluto de um arquivo: ')
        with open(arq) as f:
            res = f.read()
            break
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m Tente novamente')
vogais = len([x.lower() for x in res if x in 'ãáaeéiíoóu'])
print('- ' * 15)
print(f'O arquivo contem {vogais} vogais')