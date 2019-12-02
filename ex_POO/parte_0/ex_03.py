class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade, qtd_pessoas):
        self._andar_atual = andar_atual
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._qtd_pessoas = qtd_pessoas

    @property
    def andar_atual(self):
        return self._andar_atual

    @andar_atual.setter
    def andar_atual(self, andar):
        self._andar_atual = andar

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def qtd_pessoas(self):
        return self._qtd_pessoas

    @qtd_pessoas.setter
    def qtd_pessoas(self, value):
        self._qtd_pessoas = value

    def entra(self):
        if self._qtd_pessoas < self._capacidade:
            self._qtd_pessoas += 1
        else:
            print('Elevador lotado')

    def sai(self):
        if self._qtd_pessoas > 0:
            self._qtd_pessoas -= 1
        else:
            print('Elevador vazio')

    def sobe(self):
        if self._andar_atual < self._total_andares:
            self._andar_atual += 1
        else:
            print('Elevador no último andar')

    def desce(self):
        if self._andar_atual > 0:
            self._andar_atual -= 1
        else:
            print('Elevador no térreo')


elevador1 = Elevador(5, 12, 8, 4)
elevador1.sobe()
elevador1.desce()
elevador1.qtd_pessoas = 8
elevador1.entra()
print('- ' * 15)
elevador1.sai()
print(elevador1.qtd_pessoas)
elevador1.andar_atual = 0
elevador1.desce()
print('- ' * 15)
