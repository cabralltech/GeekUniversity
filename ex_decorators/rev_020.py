from validacao import validar, go_on


class Turma:
    @validar(ValueError)
    def __init__(self):
        self.num = int(input('Quantidade de alunxs na turma: ').strip())
        self.nomes = [self.nom() for x in range(self.num)]
        self.notas = [self.nota() for y in range(self.num)]

    def __repr__(self):
        return f'{self.nomes}\n{self.notas}'

    @validar(ValueError)
    def nom(self):
        nome = input('Nome: ').title().strip()
        return nome

    @validar(ValueError)
    def nota(self):
        nota = float(input('Nota final: ').strip().replace(',', '.'))
        return nota

mate = Turma()
print(mate)
