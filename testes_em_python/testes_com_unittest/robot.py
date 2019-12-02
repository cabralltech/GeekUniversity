class Robot:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__hobilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100
        return self.__bateria

    def dizer_nome(self):
        if self.__bateria > 10:
            return f'BEEP BOOP - Meu nome é {self.__nome}'

    def aprender_habilidades(self, nova_habilidade, custo):
        if custo < self.__bateria:
            self.__bateria -= custo
            return f'Mega-man sabe {nova_habilidade} agora'
        return 'Bateria insuficiente, recarregue a bateria'

