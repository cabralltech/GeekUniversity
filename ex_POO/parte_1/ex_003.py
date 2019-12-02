from validacao import validar


class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.__lado * self.__lado

    def calcular_perimetro(self):
        return self.__lado * 4

    def imprimir(self):
        print('- ' * 5)
        print(f'Medidas quadrado:\n'
              f'Lado: {self.__lado}\n'
              f'Área: {self.__area}\n'
              f'Perímetro: {self.__perimetro}')


quad = Quadrado(2.5)
quad.imprimir()