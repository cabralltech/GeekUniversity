class Equipamento:
    def __init__(self, departamento, usuario):
        self.__departamento = departamento
        self.__usuario = usuario

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, outro):
        self.__departamento = outro

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, outro):
        self.__usuario = outro

    def exibir(self):
        return f'{self.__departamento} - {self.__usuario}'


class Computador(Equipamento):
    def __init__(self, departamento, usuario, marca, sistema):
        super().__init__(departamento, usuario)
        self.__marca = marca
        self.__sistema = sistema

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, outra):
        self.__marca = outra

    @property
    def sistema(self):
        return self.__sistema

    @sistema.setter
    def sistema(self, outro):
        self.__sistema = outro

    def exibir(self):
        return f'Computador: {super().exibir()}\nMarca e sistema: {self.__marca} - {self.__sistema}'


class TestaEquipamento:
    def __init__(self):
        dep = input('Departamento: ').strip().title()
        user = input('Usuário: ').strip().title()
        self.equipo = Equipamento(dep, user)
        marca = input('Marca: ').strip().title()
        sist = input('Sistema Operacional: ').strip().title()
        self.comp = Computador(dep, user, marca, sist)

    def main(self):
        print('- ' * 15)
        print(self.comp.exibir())


teste1 = TestaEquipamento()
teste1.main()
