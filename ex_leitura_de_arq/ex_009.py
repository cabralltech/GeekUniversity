def validate(fn):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except FileNotFoundError:
                print('\033[31mArquivo não encontrado!\033[m Tente novamente')
    return wrapper


@validate
def path():
    p = input('Digite o path absoluto de um arquivo de texto: ')
    with open(p) as f:
        file = f.read()
    return file


con_1 = path()
con_2 = path()
n = input('Digite o nome de um novo arquivo: ')
nome = n + '.txt'
with open(nome, 'a') as novo:
    novo.write(con_1)
    novo.write(con_2)
with open(nome) as nv:
    arq = nv.read()
print(arq)
