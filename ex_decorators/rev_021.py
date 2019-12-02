from validacao import validar
import os


class Alunx(dict):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self["nome"] = input('Nome: ').strip().title()
        self["nota"] = float(input('Nota final: ').strip().replace(',', '.'))


class Turma(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        pa = 'lista_alunxs.bin'
        if os.path.exists(pa):
            with open(pa, 'rb') as tl:
                for a in tl:
                    alu = a.decode().replace('\n', '').split(':')
                    al = {'nome': alu[0].strip(), 'nota': float(alu[1].strip())}
                    self.append(al)
        else:
            num = int(input('Quantidade de alunxs na turma: ').strip())
            for i in range(num):
                print('- ' * 15)
                self.append(Alunx())

    def __repr__(self):
        return super().__repr__()

    def gravar(self):
        with open('lista_alunxs.bin', 'wb') as turma:
            for alun in self:
                turma.write(f'{alun["nome"]:<40}: {alun["nota"]} \n'.encode())

    def maior_nota(self):
        return f'A maior nota da turma é {max(self, key=lambda a: a["nota"])["nota"]} ' \
            f'dx alunx {max(self, key=lambda b: b["nota"])["nome"]}'


lista = Turma()
# lista.gravar()
print(lista.maior_nota())