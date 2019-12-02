while True:
    try:
        file = input('Digite o path absoluto de um arquivo texto: ')
        with open(file) as f:
            res = f.read()
            break
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m Tente novamente')
vogais = 'aáãéeiíoóõuú'
vog = len([x.lower() for x in res if x in vogais])
consoantes = 'bcdfghjklmnpqrstwvxyz'
con = len([y.lower() for y in res if y in consoantes])
print('- ' * 15)
print(f'O arquivo contem {vog} vogais e {con} consoantes')