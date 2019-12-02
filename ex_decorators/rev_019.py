from validacao import validar, go_on
import os


class Alunx(dict):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self['nome'] = input('Nome: ').strip().title()
        self['nota'] = float(input('Nota: ').strip().replace(',', '.'))

    def __repr__(self):
        return f'NOME: {self["nome"]} - NOTA: {self["nota"]}'


class Turma(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        if os.path.exists('notas_alunx.txt'):
            with open('notas_alunx.txt') as ns:
                for alun in ns:
                    alunx = alun.replace('\n', '').replace('NOME:', '').replace('NOTA:', '').split('-')
                    al = {'nome': alunx[0].strip(), 'nota': float(alunx[1].strip())}
                    self.append(al)
        else:
            while True:
                print('- ' * 15)
                self.append(Alunx())
                if go_on('alunx') == 'N':
                    break

    def __repr__(self):
        return super().__init__()

    def salvar(self):
        with open('notas_alunx.txt', 'w') as na:
            for a in self:
                na.write(f'{a} \n')

    def maior_nota(self):
        return f'A maior nota da turma é {max(self, key=lambda a: a["nota"])["nota"]} ' \
            f'dx alunx {max(self, key=lambda b: b["nota"])["nome"]}'


lista = Turma()
print('- ' * 15)
# lista.salvar()
print(lista.maior_nota())
