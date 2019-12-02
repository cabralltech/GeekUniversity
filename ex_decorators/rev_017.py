from validacao import validar, validate


class Matriz(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self.linhas = int(input('Linhas: ').strip())
        self.colunas = int(input('Colunas: ').strip())
        self.matriz = [[1 for x in range(self.colunas)] for y in range(self.linhas)]

    def __repr__(self):
        return f'{self.linhas} X {self.colunas}\n' \
            f'{self.anul}'

    @validar(ValueError)
    def anuladas(self):
        qtd = int(input('Quantas posições a serem anuladas? ').strip())
        self.anul = []
        for p in range(qtd):
            lin = int(input(f'Linha da {p+1}ª pos: ').strip())
            col = int(input(f'Coluna da {p+1}ª pos: ').strip())
            self.anul.append([lin, col])
        return self.anul

    def printar(self):
        for l in range(len(self.matriz)):
            for c in range(self.linhas):
                if [l, c] in self.anul:
                    self.matriz[l][c] = 0
                print(f'{self.matriz[l][c]:^5}', end=' ')
            print()

    def gravar_ent(self):
        with open('matriz_entrada.txt', 'w') as me:
            me.write(self.__repr__())

    @staticmethod
    def gravar_saida():
        with open('matriz_entrada.txt') as me:
            info = me.readlines()
        dim = [int(x) for x in info[0] if x.isnumeric()]
        anu = [int(z) for z in info[1] if z.isnumeric()]
        anuladas = []
        for i in range(0, len(anu), 2):
            if i < len(anu)-1:
                anuladas.extend([[anu[i], anu[i+1]]])
        with open('matriz_saida.txt', 'a') as ms:
            for li in range(dim[0]):
                for co in range(dim[1]):
                    if [li, co] in anuladas:
                        ms.write(f'{0:^5} ')
                    else:
                        ms.write(f'{1:^5} ')
                ms.write('\n')


mat = Matriz()
mat.anuladas()
print('- ' * 15)
print(mat)
print('- ' * 15)
mat.printar()
mat.gravar_ent()
mat.gravar_saida()
