import cadastro as c
import os


class Alunx(dict):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        print('- ' * 15)
        self['nome'] = input('Nome completo: ').strip().title()
        self['notas'] = [float(input(f'{x+1}ª Nota: ').replace(',', '.').strip())
                         for x in range(2)]
        self['média'] = round(sum(self['notas']) / len(self['notas']), 1)

    def __repr__(self):
        return f'{self["nome"]} - {self["notas"][0]}, {self["notas"][-1]}'


class Turma(list):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        self.disc = input('Disciplina: ').lower().strip()
        path = os.path.join(os.getcwd(), f'turma_{self.disc}.txt')
        if os.path.exists(path):
            with open(f'turma_{self.disc}.txt') as t:
                for alunx in t:
                    alunx = alunx.replace('\n', '').strip().split('-')
                    n = alunx[1].split(',')
                    al = {'nome': alunx[0].strip(),
                          'notas': [float(n[a].strip()) for a in range(2)]}
                    al['média'] = round(sum(al['notas']) / len(al['notas']), 1)
                    self.append(al.copy())
        else:
            while True:
                self.append(Alunx())
                if c.go_on('alunx') == 'N':
                    break

    def __repr__(self):
        return super().__repr__()

    @c.validate(ValueError)
    def menu(self):
        print('- ' * 15)
        opt = int(input('Escolha a operação:\n'
                        '[ 1 ] Informações sobre a turma\n'
                        '[ 2 ] Inserir nota e alunx\n'
                        '[ 3 ] Alunx e média\n'
                        '[ 4 ] Alunxs aprovadxs\n'
                        '[ 5 ] Alunxs reprovadxs\n'
                        '[ 6 ] Salvar relatório\n'
                        '[ 7 ] Sair do programa\n'
                        'Digite a opção: ').strip())
        print('- ' * 15)
        if opt == 1:
            return self._infos()
        elif opt == 2:
            self._inserir()
            self._salvar()
        elif opt == 3:
            self._media()
        elif opt == 4:
            self._aprovadxs()
        elif opt == 5:
            self._reprovadxs()
        elif opt == 6:
            self._salvar()
        elif opt == 7:
            print('PROGRAMA ENCERRADO')
        else:
            print('\033[31mOpção inválida\033[m Tente novamente')
            return self.menu()

    def _infos(self):
        print(f'Disciplina: {self.disc.title()}\nNúmero de alunos: {len(self)}')

    def _inserir(self):
        return self.append(Alunx())

    @c.validate(ValueError)
    def _media(self):
        nome = input('Nome completo dx alunx: ').strip().title()
        for a in self:
            if nome in a['nome'] or nome == a['nome']:
                print(f'{a["nome"]}: média {a["média"]}')

    def _aprovadxs(self):
        for al in self:
            if al["média"] > 6:
                print(f'- {al["nome"]}')

    def _reprovadxs(self):
        for al in self:
            if al['média'] < 6:
                print(f'- {al["nome"]}')

    def _salvar(self):
        with open(f'turma_{self.disc}.txt', 'w') as turma:
            for t in sorted(self, key=lambda b: b['nome']):
                turma.write(f'{t["nome"]} - '
                            f'{t["notas"][0]}, '
                            f'{t["notas"][1]} \n')


mat = Turma()
mat.menu()
