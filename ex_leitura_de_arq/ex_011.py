def validate(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except FileNotFoundError:
            print('\033[31mArquivo não encontrado!\033[m Tente novamente')
    return wrapper


@validate
def path():
    arq = input('Digite o path absoluto de um arquivo texto: ')
    return arq


def conta_palavra(file, palavra):
    with open(file) as f:
        arquivo = f.read().lower()
    cont = arquivo.count(palavra)
    return cont


texto = path()
pal = input('Digite palavra ser contada: ')
res = conta_palavra(texto, pal)
print('- ' * 15)
print(f'A palavra {pal} aparece {res} vezes no texto')
