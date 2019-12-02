from random import randint


class Televisor:
    def __init__(self,  marca, polegadas, canais):
        self.__ligado = False
        self.__marca = marca
        self.__polegadas = polegadas
        self.__canal = randint(0, canais)
        self.__max_canal = canais
        self.__volume = self._volume()

    def imprimir(self):
        print(f'Televisor {self.__marca} de {self.__polegadas} polegadas\n'
              f'{self.__max_canal} canais', end=' - ')
        if self.__ligado:
            print(f'Aparelho {self._checa_ligado()} no canal {self.__canal} e volume {self.__volume}')
        else:
            print(f'Aparelho {self._checa_ligado()}')

    def _volume(self):
        return randint(0, 60)

    def ligar_desligar(self):
        if self.__ligado:
            self.__ligado = False
        else:
            self.__ligado = True

    def canal_acima(self):
        if self.__canal < self.__max_canal:
            self.__canal += 1
        else:
            print(f'Canal inexistente, {self.__max_canal} é o último canal')

    def canal_abaixo(self):
        if self.__canal > 0:
            self.__canal -= 1
        else:
            print(f'Canal inexistente, {self.__canal} é o primeiro canal')

    def volume_acima(self):
        if self.__volume < 60:
            self.__volume += 1
        else:
            print(f'{self.__volume} é o volume máximo')

    def volume_abaixo(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print(f'{self.__volume} é o volume mínimo')

    def _checa_ligado(self):
        if self.__ligado:
            return 'ligado'
        return 'desligado'


tv = Televisor('Samsung', 52, 105)
tv.imprimir()
print('- ' * 15)
tv.ligar_desligar()
tv.imprimir()
tv.canal_abaixo()
tv.volume_abaixo()
print('- ' * 15)
tv.imprimir()
