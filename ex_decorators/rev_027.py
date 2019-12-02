from validacao import validar, go_on
from os import path


@validar(ValueError)
def entrada_alunx():
    print('- ' * 15)
    mat = int(input('Número de matrícula: ').strip())
    nome = input('Nome completo: ').strip().title()
    notas = [float(input(f'{x+1}ª nota: ').strip().replace(',', '.')) for x in range(2)]
    return Alunx(mat=mat, nome=nome, notas=notas)


@validar(ValueError)
def entrada_turma():
    num = int(input('Número de alunxs para cadastro: ').strip())
    disc = input('Disciplina: ').strip().title()
    prof = input('Professor(a): ').strip().title()
    return Turma(num=num, disc=disc, prof=prof)


class Alunx(dict):
    def __init__(self, mat, nome, notas):
        super().__init__()
        self['mat'] = mat
        self['nome'] = nome
        self['notas'] = notas

    def media(self):
        return round(sum(self['notas'])/len(self['notas']), 1)


class Turma(list):
    def __init__(self, num, disc, prof):
        super().__init__()
        self.num = num
        self.disc = disc
        self.prof = prof
        self.pa = 'matematica.txt'
        if path.exists(self.pa):
            with open(self.pa) as arq:
                for alunx in arq:
                    alunx = alunx.replace('\n', '').strip().split(':')
                    self.append(Alunx(
                        mat=int(alunx[0].strip()),
                        nome=alunx[1].strip(),
                        notas=[float(x.strip()) for x in alunx[2].replace('[', '').replace(']', '').split(',')]
                    ))
            self._menu()
        else:
            self._cadastrar()
            self._gravar()

    def __repr__(self):
        return super().__repr__()

    def _cadastrar(self):
        while True:
            self.append(entrada_alunx())
            if go_on('alunx') == 'N':
                break

    def _gravar(self):
        with open(self.pa, 'w') as mat:
            for alunx in sorted(self, key=lambda a: a['nome']):
                mat.write(f'{alunx["mat"]:<5}: '
                          f'{alunx["nome"]:40}: '
                          f'{alunx["notas"]} \n')

    @validar(ValueError)
    def _menu(self):
        menu = int(input('Escolha a operação:\n'
                         '[ 1 ] Dados da turma\n'
                         '[ 2 ] Inserir aluno\n'
                         '[ 3 ] Alunxs e médias\n'
                         '[ 4 ] Alunxs aprovadxs\n'
                         '[ 5 ] Alunxs reprovadxs\n'
                         '[ 6 ] Salvar dados\n'
                         '[ 7 ] Sair do programa\n'
                         'Digite a opção: ').strip())
        print('- ' * 15)
        if menu == 1:
            self.num = len(self)
            print(f'Disciplina: {self.disc.upper()}\n'
                  f'Professor(a): {self.prof.title()}\n'
                  f'Número de alunxs: {self.num}\n')
        elif menu == 2:
            self.append(entrada_alunx())
            self._gravar()
        elif menu == 3:
            self._printar_turma()
        elif menu == 4:
            for alunx in self:
                if alunx.media() > 6.0:
                    print(f'- {alunx["mat"]:<5}'
                          f'{alunx["nome"]}')
        elif menu == 5:
            for alunx in self:
                if alunx.media() < 6.0:
                    print(f'- {alunx["mat"]:<5}'
                          f'{alunx["nome"]}')
        elif menu == 6:
            self._gravar()
        elif menu == 7:
            print(f'{"PROGRAMA ENCERRADO":^30}')
            print('- ' * 15)
        else:
            print('\033[31mOpção inválida\033[m Tente novamente')
            self._menu()

    def _printar_turma(self):
        for alunx in self:
            print(f'{alunx["mat"]:<5}:'
                  f'{alunx["nome"]:<40}'
                  f'{alunx.media()}')


if __name__ == '__main__':
    if not path.exists('matematica.txt'):
        matematica = entrada_turma()
    else:
        matematica = Turma(4, 'matemática', 'Mhirley Lopes')
