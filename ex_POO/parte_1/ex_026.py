from time import sleep


class Microondas:
    def __init__(self, marca, litros):
        self.__marca = marca
        self.__litros = litros
        self.__ligado = False
        self.__porta_fechada = True

    def __repr__(self):
        return f'Microondas {self.__marca} com {self.__litros}l'

    def ligar_desligar(self):
        if self.__ligado:
            self.__ligado = False
            print('Aparelho foi desligado corretamente')
        else:
            if self.__porta_fechada:
                self.__ligado = True
                print(f'Aparelho {self._checa_ligado()}')
            else:
                print('Favor fechar a porta para ligar o aparelho')

    def fechar_porta(self):
        if self.__porta_fechada:
            self.__porta_fechada = False
            print('Porta aberta!')
        else:
            self.__porta_fechada = True
            print('Porta fechada')

    def _checa_ligado(self):
        if self.__ligado:
            return 'ligado'
        return 'desligado'

    def _checa_porta(self):
        if self.__porta_fechada:
            return 'com porta fechada'
        return 'com porta aberta, favor fechar a porta!'

    def imprimir(self):
        print('- ' * 15)
        print(f'Microondas, marca: {self.__marca} com {self.__litros}l')
        if self._checa_ligado():
            print(f'Aparelho {self._checa_ligado()} e {self._checa_porta()}')
        else:
            print(f'Aparelho {self._checa_ligado()} e {self._checa_porta()}')


micro = Microondas('Panasonic', 3.5)
micro.imprimir()
print('- ' * 5)
# micro.fechar_porta()
micro.ligar_desligar()
micro.imprimir()

