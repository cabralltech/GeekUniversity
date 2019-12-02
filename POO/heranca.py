class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__matricula}: {super().nome_completo()} - CPF {self._Pessoa__cpf}'


cliente1 = Cliente('Mhirley', 'Lopes', '123.456.789-00', 3500.00)
funcionario1 = Funcionario('Gustavo', 'Cabeza', '098.765.432-11', 1234)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print('- ' * 15)
print(cliente1.__dict__)
print('- ' * 15)
print(funcionario1.__dict__)
print('- ' * 15)
print(funcionario1.nome_completo())
