def validate(fn):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


class Matriz:
    @validate
    def __init__(self):
        self.linhas = int(input('Número de linhas: '))
        self.colunas = int(input('Número de colunas: '))
        print('- ' * 15)
        self._anuladas()
        self.matriz = [[0 if (y, x) in self.pos else 1
                        for x in range(self.colunas)]
                       for y in range(self.linhas)]

    def __repr__(self):
        return f'Matriz de dimensões {self.linhas} X {self.colunas}\n' \
            f'{self.num} posições anuladas: {self.pos}'

    @validate
    def _anuladas(self):
        self.num = int(input('Número de posições anuladas: '))
        self.pos = []
        for i in range(self.num):
            print(f'Posição {i+1}')
            print('- ' * 5)
            lin = int(input('Linha: '))
            col = int(input('Coluna: '))
            self.pos.append((lin, col))
        return self.pos

    def printar(self):
        for l in range(len(self.matriz)):
            for c in range(self.linhas):
                print(f'[{self.matriz[l][c]:^5}]', end='')
            print()


# with open('matriz.txt', 'a') as m:
#     mat = Matriz()
#     m.write(repr(mat))
with open('matriz.txt') as m:
    dim = [int(x) for x in m.readlines()[0] if x.isnumeric()]
    m.seek(0)
    anu = [int(y) for y in m.readlines()[1][5:] if y.isnumeric()]
    anu = [[anu[a], anu[a+1]] for a in range(0, len(anu)-1, 2)]
with open('matriz_saida.txt', 'w')as ma:
    mat2 = [[0 if [b, c] in anu else 1
             for c in range(dim[0])]
            for b in range(dim[1])]
    for lin in range(len(mat2)):
        for col in range(dim[0]):
            ma.write(f'[{mat2[lin][col]:^5}]')
        ma.write('\n')

