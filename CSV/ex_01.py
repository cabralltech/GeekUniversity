class Pessoa:
    def __init__(self, nome, idade, altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    def __repr__(self):
        return f'{self.nome} tem {self.idade} anos e {self._altura}m de altura'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, age):
        self._idade = age

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, height):
        self._altura = height

    def printar_dados(self):
        print('- ' * 15)
        print(f'Nome: {self._nome}\n'
              f'Idade: {self._idade} anos\n'
              f'Altura: {self._altura}m\n')

if __name__ == '__main__':
    p1 = Pessoa('Mhirley Lopes', 40, 1.73)
    p1.nome = 'Mhirley Mansur Gonzaga Lopes'
    print('- ' * 15)
    print(p1)
    p1.idade = 43
    print('- ' * 15)
    print(p1)
    p1.altura = 1.75
    p1.nome = 'Mhirley M G Lopes'
    print('- ' * 15)
    print(p1)
    p1.printar_dados()


