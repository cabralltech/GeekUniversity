from validacao import validar, go_on
from os import path


@validar(ValueError)
def entrada():
    print('- ' * 15)
    nome = input('Primeiro nome: ').strip().title()
    sobrenome = input('Sobrenome: ').strip().title()
    fone = int(input('Telefone: ').strip())
    print('Data de aniversário')
    print('- ' * 5)
    dia = int(input('Dia: ').strip())
    mes = int(input('Mês: ').strip())
    ano = int(input('Ano: ').strip())
    aniver = [dia, mes, ano]
    return Contato(nome=nome, sobrenome=sobrenome, fone=fone, aniver=aniver)


class Contato(dict):
    @validar(ValueError)
    def __init__(self, nome, sobrenome, fone, aniver):
        super().__init__()
        self["nome"] = nome
        self['sobrenome'] = sobrenome
        self['fone'] = fone
        self['aniver'] = aniver

    def __repr__(self):
        return super().__repr__()

    def aniver(self):
        return f'{self["aniver"][0]}/{self["aniver"][1]}/{self["aniver"][2]}'

    def fullname(self):
        return f'{self["nome"]} {self["sobrenome"]}'


class Agenda(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self.agenda = 'agenda.bin'
        if not path.exists(self.agenda):
            while True:
                self.append(entrada())
                if go_on('contato') == 'N':
                    break
            with open(self.agenda, 'w+b') as agenda_criar:
                for contato in self:
                    agenda_criar.write(f'{contato.fullname():<40}: '
                                       f'{contato["fone"]:<15}: '
                                       f'{contato.aniver()} \n'.encode())
        else:
            with open(self.agenda, 'rb') as agenda_bin:
                for contato in agenda_bin:
                    contato = contato.decode().replace('\n', '').split(':')

                    contato = Contato(
                        nome=contato[0].strip().split()[0],
                        sobrenome=contato[0].strip().split()[1],
                        fone=int(contato[1].strip()),
                        aniver=[int(x) for x in contato[2].strip().split('/') if x.isnumeric()]
                    )
                    self.append(contato)
            self._menu()
            self._gravar()

    def __repr__(self):
        return super().__repr__()

    @validar(ValueError)
    def _menu(self):
        menu = int(input('Escolha a operação:\n'
                         '[ 1 ] inserir contato\n'
                         '[ 2 ] remover contato\n'
                         '[ 3 ] pesquisar contato pelo nome\n'
                         '[ 4 ] listar todxs xs contatos\n'
                         '[ 5 ] imprimir aniversariantes do mês\n'
                         'Digite a opção: ').strip())
        print('- ' * 15)
        if menu == 1:
            self._inserir()
        elif menu == 2:
            self._remover()
        elif menu == 3:
            self._pesquisar()
        elif menu == 4:
            self._listar()
        elif menu == 5:
            self._aniver_mes()
        else:
            print('\033[31mOpção inválida\033[m Tente novamente')
            self._menu()

    def _inserir(self):
        self.append(entrada())

    def _remover(self):
        nome_remover = input('Primeiro nome do contato a ser apagado: ').strip().title()
        for indice, contato in enumerate(self):
            if contato['nome'] == nome_remover:
                print(f'- {contato.fullname()}')
                sobrenome_remover = input('Sobrenome do contato a ser apagado: ').strip().title()
                if contato['sobrenome'] == sobrenome_remover:
                    contato_removido = self.pop(indice)
                    print(f'{contato_removido.fullname()} foi apagado com sucesso')

    def _pesquisar(self):
        nome_pesquisa = input('Primeiro nome contato: ').strip().title()
        for indice, contato in enumerate(self):
            if contato['nome'] == nome_pesquisa:
                print(f'- {contato.fullname()}')
                sobrenome_pesquisa = input('Sobrenome: ').strip().title()
                if contato['sobrenome'] == sobrenome_pesquisa:
                    print('- ' * 5)
                    print(f'Nome: {contato.fullname()}\n'
                          f'Telefone: {contato["fone"]}\n'
                          f'Aniversário: {contato.aniver()}')

    def _listar(self):
        for contato in self:
            print(f'- {contato.fullname()}')

    @validar(ValueError)
    def _aniver_mes(self):
        mes_listar = int(input('Digite o mês: ').strip())
        print('- ' * 15)
        for contato in self:
            if contato['aniver'][1] == mes_listar:
                print(f'- {contato.fullname()}')

    def _gravar(self):
        with open(self.agenda, 'w+b') as agenda_gravar:
            for contato in sorted(self, key=lambda a: a['nome']):
                agenda_gravar.write(f'{contato.fullname():<40}: '
                                    f'{contato["fone"]:<15}: '
                                    f'{contato.aniver()} \n'.encode())


mhiloca = Agenda()
