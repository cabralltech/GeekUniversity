from math import pi


class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__area = self.calcular_area()
        self.__circunferencia = self.calcular_circunferencia()

    def calcular_area(self):
        return pi * (self.__raio ** 2)

    def calcular_circunferencia(self):
        return pi * 2 * self.__raio

    def imprimir(self):
        print('- ' * 10)
        print(f'Medidas círculo:\n'
              f'Raio: {self.__raio}\n'
              f'Área: {round(self.__area, 1)}\n'
              f'Circunferência: {round(self.__circunferencia, 1)}')


circ = Circulo(3.6)
circ.imprimir()