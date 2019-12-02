class Moto:
    def __init__(self,marca, modelo, cor, cambio,  marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__cambio = [x for x in range(cambio+1)]
        self.__marcha = marcha
        self.__ligada = False

    def __repr__(self):
        return f'{"- " * 5}\n' \
               f'Marca: {self.__marca.title()}\n' \
               f'Modelo: {self.__modelo}\n' \
               f'Cor: {self.__cor}\n' \
               f'Câmbio: {len(self.__cambio)-1} marchas\n' \
               f'Marcha atual: {self.__marcha}\n' \
               f'On/Off: {self.__ligada}'

    def marcha_acima(self):
        if self.__marcha < max(self.__cambio):
            self.__marcha += 1
        else:
            print('- ' * 5)
            print('Marcha inexistente')

    def marcha_abaixo(self):
        if self.__marcha > 0:
            self.__marcha -= 1
        else:
            print('- ' * 5)
            print('Marcha inexistente')

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

    def checa_ligada(self):
        if self.__ligada:
            return 'Moto ligada'
        return 'Moto desligada'


moto = Moto('Honda', 'CG 160 Fan', 'preta', 5, 3)
moto.ligar_desligar()
print(moto)
moto.marcha_acima()
print(moto)
moto.ligar_desligar()
print(moto.checa_ligada())
