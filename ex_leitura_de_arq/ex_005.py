class Arquivo:
    def __init__(self):
        while True:
            try:
                path = input('Digite um path absoluto: ')
                with open(path) as p:
                    file = p.read()
                    break
            except FileNotFoundError:
                print('\033[31mArquivo não encontrado!\033[m Tente novamente')
        self.file = file

    def __repr__(self):
        return self.file


class Analise:
    def __init__(self, arq, char):
        self.arq = arq
        self.char = char

    def __repr__(self):
        return f'A letra {self.char} aparece {self._occurrence()} vezes'

    def _occurrence(self):
        return self.arq.count(self.char)


arquivo = Arquivo()
print(Analise(repr(arquivo), 'a'))
