def validate(fn):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except FileNotFoundError:
                print('\033[31mArquivo não encontrado!\033[m Tente novamente')
    return wrapper


@validate
def text():
    arq = input('Digite o path absoluto de um arquivo texto: ')
    with open(arq) as a:
        arquivo = a.read()
    return arquivo


def analise(texto):
    char_count = len(texto.replace(' ', '').replace('\n', '').replace(' ', '').replace('•', ''))
    lines = len(texto.split('\n'))
    words = texto.replace('\n', ' ').replace('•', '').replace('   ', '')
    word_count = len(words.split(' '))
    return f'Número de linhas: {lines}\nNúmero de palavras: {word_count}\nNúmero de caracteres: {char_count}'


file = text()
print('- ' * 15)
print(analise(file))