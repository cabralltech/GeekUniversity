from validacao import validar, go_on
from os import path


class Alunx(dict):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self['nome'] = input('Nome: ').strip().title()
        self['notas'] = [input(f'{x+1}ª Nota: ') for x in range(3)]

    def __repr__(self):
        return super().__repr__()


class Turma(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self.pe = 'notas_entrada.txt'
        if path.exists(self.pe):
            with open(self.pe) as ne:
                for st in ne:
                    stu = st.replace('\n', '').split(':')
                    n = [float(a) for a in stu[1] if a.isnumeric()]
                    s = {'nome': stu[0].strip().title(), 'notas': n}
                    self.append(s)
        else:
            while True:
                self.append(Alunx())
                if go_on('alunx') == 'N':
                    break

    def __repr__(self):
        return super().__repr__()

    def gravar(self):
        with open(self.pe, 'w') as nf:
            for al in self:
                nf.write(f'{al["nome"]:<40}: '
                         f'{al["notas"][0]:<5}'
                         f'{al["notas"][1]:<5}'
                         f'{al["notas"][2]} \n')

    def sair(self):
        with open('notas_saida.txt', 'w') as ns:
            for stud in self:
                grades = sorted(stud['notas'])
                ns.write(f'{stud["nome"]:<40}: '
                         f'{grades[0]:<5}'
                         f'{grades[1]:<5}'
                         f'{grades[2]} \n')


lista = Turma()
# lista.gravar()
lista.sair()
