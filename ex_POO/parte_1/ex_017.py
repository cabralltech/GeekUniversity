class Eletrodomestico:
    def __init__(self, nome, marca, cor):
        self.__nome = nome
        self.__marca = marca
        self.__cor = cor
        self.__ligado = False

    def __repr__(self):
        return f'{self.__nome} da {self.__marca}: {self.__cor} - {self.checa_ligado()}'

    def liga_desliga(self):
        if self.__ligado:
            self.__ligado = False
        else:
            self.__ligado = True

    def checa_ligado(self):
        if self.__ligado:
            return 'ligado'
        return 'desligado'


eletro = Eletrodomestico('Torradeira', 'Wallita', 'branca')
print(eletro)
eletro.liga_desliga()
print('- ' * 15)
print(eletro)