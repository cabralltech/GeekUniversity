import cadastro as c


class Contato(dict):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        print('- ' * 15)
        self['nome'] = input('Nome: ').title().strip()
        self['fone'] = int(input('Telefone: ').strip())
        aniver = input('Aniversário: ').strip()
        self['aniver'] = aniver.split('/')

    def __repr__(self):
        return f'{self["nome"]} - {self["fone"]} - {self["aniver"][0]}/{self["aniver"][-1]}'


class Pesquisa(list):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        with open('agenda.bin', 'rb') as agenda:
            for dado in agenda:
                contato = dado.decode()
                contato = contato.split('-')
                conts = {'nome': contato[0].strip(),
                           'fone': contato[1].strip(),
                           'aniver': contato[2].strip().replace('\n', '').split('/')}
                self.append(conts.copy())
        self._menu()

    def __repr__(self):
        return super().__repr__()

    @c.validate(ValueError)
    def _menu(self):
        self.menu = int(input('Escolha a operação:\n'
                              '[ 1 ] inserir contato\n'
                              '[ 2 ] remover contato\n'
                              '[ 3 ] pesquisar contato\n'
                              '[ 4 ] listar contatos\n'
                              '[ 5 ] listar contatos 1ª letra\n'
                              '[ 6 ] imprimir aniversariantes mês\n'
                              'Digite a opeção: ').strip())
        print('- ' * 15)
        if self.menu == 1:
            self._inserir()
        elif self.menu == 2:
            self._remover()
        elif self.menu == 3:
            self._pesquisar()
        elif self.menu == 4:
            self._listar_contatos()
        elif self.menu == 5:
            self._listar_cont_letra()
        elif self.menu == 6:
            self._aniver_mes()
        else:
            print('\33[31mOpção inválida\033[m Tente novamente')
            self._menu()

    def _inserir(self):
        return self.append(Contato())

    def _remover(self):
        nome = input('Nome: ').strip().title()
        print('- ' * 5)
        for x in self:
            if nome in x['nome']:
                print(f'Remover {x["nome"]}?')
        res = input('Digite o nome completo para '
                    'remover contato: ').strip().title()
        for i, y in (self):
            if res in y['nome']:
                rem = self.pop(i)
                print(f'Contato {rem["nome"]} removido com sucesso')

    def _pesquisar(self):
        nom = input('Nome: ').title().strip()
        for z in self:
            if nom in z['nome']:
                print(f'Pesquisar {z["nome"]}?')
        re = input('Digite nome completo para '
                   'pesquisa: ').strip().title()
        for n in self:
            if re in n['nome']:
                print('- ' * 15)
                print(f'Nome: {n["nome"]}\n'
                      f'Telefone: {n["fone"]}\n'
                      f'Aniversário: {n["aniver"][0]}/'
                      f'{n["aniver"][1]}')

    def _listar_contatos(self):
        for i in self:
            print(f'- {i["nome"]}')

    def _listar_cont_letra(self):
        letra = input('Digite a 1ª letra: ').upper().strip()[0]
        print()
        for w in self:
            if letra in w['nome'][0]:
                print(f'- {w["nome"]}')

    @c.validate
    def _aniver_mes(self):
        mes = int(input('Digite o mês: ').strip())
        print()
        for t in self:
            if mes == int(t['aniver'][-1]):
                print(f'- {t["nome"]}')


# with open('agenda.bin', 'wb') as ag:
#     while True:
#         cont = Contato()
#         ag.write(f'{repr(cont)} \n'.encode())
#         if c.go_on('contato') == 'N':
#             break
ag = Pesquisa()
with open('agenda.bin', 'w+b') as agenda:
    for co in sorted(ag, key=lambda o: o['nome']):
        agenda.write(f'{co["nome"]} - '
                     f'{co["fone"]} - '
                     f'{co["aniver"][0]}/'
                     f'{co["aniver"][-1]}\n'.encode())
