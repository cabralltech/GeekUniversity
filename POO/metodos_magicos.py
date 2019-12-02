class Livro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __del__(self):
        return f'O livro {self.__titulo} foi apagado com sucesso'

    def __add__(self, other):
        return f'{self.__titulo} e {other._Livro__titulo}'

    def __mul__(self, other):
        if isinstance(other, int):
            quebra = ''
            for vezes in range(other):
                quebra += self.__titulo + '\n'
            return quebra
        else:
            return 'Não se pode multiplicar'


livro1 = Livro('O Idiota', 'F. Dostoievski', 465)
print(livro1)
print(len(livro1))
livro2 = Livro('Crime e Castigo', 'F. Dostoievski', 436)
print(livro1 + livro2)
print(livro2 * 3)
