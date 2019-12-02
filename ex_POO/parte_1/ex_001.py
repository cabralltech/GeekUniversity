class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print('- ' * 15)
        print(f'Nome: {self.__nome}\n'
              f'Endereço: {self.__endereco}\n'
              f'Telefone: {self.__telefone}')


mhi = Pessoa('Mhirley Lopes', 'Rua Almirante Lamego', 48996153258)
mhi.imprimir()
