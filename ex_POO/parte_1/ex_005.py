class Retangulo:
    def __init__(self, largura, comprimento):
        self.__largura = largura
        self.__comprimento = comprimento
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.__largura * self.__comprimento

    def calcular_perimetro(self):
        return 2 * self.__largura + 2 * self.__comprimento

    def imprimir(self):
        print('- ' * 5)
        print(f'Medidas retângulo:\n'
              f'Largunra: {self.__largura}\n'
              f'Comprimento: {self.__comprimento}\n'
              f'Área: {self.__area}\n'
              f'Perímetro: {self.__perimetro}')


rect = Retangulo(2.5, 4.5)
rect.imprimir()