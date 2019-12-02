from validacao import validar


@validar(ValueError)
def entrada_pessoa():
    print('- ' * 15)
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: ').strip())
    altura = float(input('Altura (em metros): ').replace(',', '.').strip())
    return Pessoa(nome, idade, altura)


class Pessoa:
    def __init__(self, nome, idade, altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura


class Agenda(list):
    def __init__(self):
        super().__init__()
        for pessoa in range(10):
            self.append(entrada_pessoa())

    @validar(ValueError)
    def menu(self):
        menu = int(input('Escolha a operação:\n'
                         '[ 1 ] inserir pessoa\n'
                         '[ 2 ] remover pessoa\n'
                         '[ 3 ] buscar pessoa\n'
                         '[ 4 ] imprimir agenda\n'
                         '[ 5 ] imprimir pessoa\n'
                         'Digite a operação: ').strip())
        if menu == 1:
            self._inserir()
        elif menu == 2:
            self._remover()
        elif menu == 3:
            self._busca()
        elif menu == 4:
            self._imprimir_agenda()
        elif menu == 5:
            self._imprimir_pessoa()
        else:
            print('\033[31mOpção inválida\033[m Tente novamente')
            self.menu()

    def _inserir(self):
        self.append(entrada_pessoa())

    def _remover(self):
        name = input('Nome pessoa a ser removida: ').strip().title()
        for pessoa in self:
            if name == pessoa.nome or name in pessoa.nome:
                removed = self.pop(pessoa)
                return f'{pessoa._nome} foi removido com sucesso'

    def _busca(self):
        name = input('Nome pessoa: ').strip().title()
        for indice, pessoa in enumerate(self):
            if name == pessoa.nome or name in pessoa.nome:
                return f'{pessoa.nome} está na {indice+1}ª posição'

    def _imprimir_agenda(self):
        for pessoa in self:
            print(f'- {pessoa.nome}')

    def _imprimir_pessoa(self):
        name = input('Nome: ').strip().title()
        for pessoa in self:
            if name in pessoa.nome or name == pessoa.nome:
                print(f'Nome: {pessoa.nome}\n'
                      f'Idade: {pessoa.idade} anos\n'
                      f'Altura: {pessoa.altura}m')


agenda = Agenda()
agenda.menu()