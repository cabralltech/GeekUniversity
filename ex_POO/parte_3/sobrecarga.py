from validacao import validar


class Pessoa:
    def __init__(self, codigo, nome, idade):
        print('Contrutor Padrão')
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        self.exibe(1)

    def exibe(self, num=0):
        print('- ' * 5)
        if num == 1:
            print(f'Código: {self.__codigo}\n'
                  f'Nome: {self.__nome}\n'
                  f'Idade: {self.__idade} anos')
        else:
            print(f'Código: {self.__codigo}\n'
                  f'Nome: {self.__nome}')


class TestePessoa:
    @validar(ValueError)
    def __init__(self):
        print('Segundo Construtor')
        cod = int(input('Código: ').strip())
        nom = input('Nome: ').strip().title()
        ida = int(input('Idade: ').strip())
        pessoa1 = Pessoa(cod, nom, ida)


p1 = TestePessoa()