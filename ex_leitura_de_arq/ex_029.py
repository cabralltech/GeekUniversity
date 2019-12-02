import cadastro as c
import os


class Vendedor(dict):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        print('- ' * 15)
        self['codigo'] = int(input('Código do vendedor: ').strip())
        self['nome'] = input('Nome completo: ').strip().title()
        self['venda'] = float(input('Valor venda: ').replace(',', '.').strip())
        self['mes'] = int(input('Mês: ').strip())

    def __repr__(self):
        return super().__repr__()


class Vendas(list):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        if os.path.exists(os.path.join(os.getcwd(), 'vendas.txt')):
            with open('vendas.txt') as v:
                for vendedor in v:
                    ve = vendedor.replace('\n', '').split('-')
                    rela = {
                        'codigo': int(ve[0].strip()),
                        'nome': ve[1].strip(),
                        'venda': float(ve[2].strip()),
                        'mes': int(ve[3].strip())
                    }
                    self.append(rela)
            self._menu()
        else:
            while True:
                self.append(Vendedor())
                if c.go_on('vendedor') == 'N':
                    break
            self._menu()

    @c.validate(ValueError)
    def _menu(self):
        print('- ' * 15)
        self.menu = int(input('Escolha a operação:\n'
                              '[ 1 ] Criar arquivo\n'
                              '[ 2 ] Incluir registro\n'
                              '[ 3 ] Excluir vendedor\n'
                              '[ 4 ] Alterar valor de venda\n'
                              '[ 5 ] Imprimir na tela de saída\n'
                              '[ 6 ] Excluir arquivo\n'
                              '[ 7 ] Sair do programa\n'
                              'Digite a opção: ').strip())
        print('- ' * 15)
        if self.menu == 1:
            self._salvar()
        elif self.menu == 2:
            self._inserir()
        elif self.menu == 3:
            self._excluir()
        elif self.menu == 4:
            self._alterar()
        elif self.menu == 5:
            self._printar()
        elif self.menu == 6:
            self._apagar_arquivo()
        elif self.menu == 7:
            print('PROGRAMA ENCERRADO')
        else:
            print('\033[31mOpção inválida\033[m')

    def _salvar(self):
        if os.path.exists(os.path.join(os.getcwd(), 'vendas.txt')):
            with open('vendas.txt', 'r+') as v:
                for venda in sorted(self, key=lambda a: a["codigo"]):
                    v.write(f'{venda["codigo"]} - '
                            f'{venda["nome"]} - '
                            f'{venda["venda"]} - '
                            f'{venda["mes"]} \n')
        else:
            with open('vendas.txt', 'w') as v:
                for venda in sorted(self, key=lambda a: a["codigo"]):
                    v.write(f'{venda["codigo"]} - '
                            f'{venda["nome"]} - '
                            f'{venda["venda"]} - '
                            f'{venda["mes"]} \n')

    def _inserir(self):
        self.append(Vendedor())
        self._salvar()

    @c.validate(ValueError)
    def _excluir(self):
        nome = input('Nome do vendedor: ').strip().title()
        for vendedor in self:
            if nome in vendedor['nome'] or nome == vendedor['nome']:
                print(f'{vendedor["codigo"]} - {vendedor["nome"]}')
        cod = int(input('Código de vendedor para exclusão: ').strip())
        for x, codigo in enumerate(self):
            if cod == codigo['codigo']:
                v = self.pop(x)
                self._salvar()
                print(f'Vendedor {v["nome"]} removido com sucesso')
        self._salvar()

    @c.validate(ValueError)
    def _alterar(self):
        self._printar()
        valor = float(input('Valor de venda a ser alterado: ').replace(',', '.').strip())
        for item in self:
            if item['venda'] == valor:
                print(f'{item["nome"]}: {item["venda"]}')
                item['venda'] = float(input('Novo valor: ').replace(',', '.').strip())
                print(f'R$ {item["venda"]} - Valor alterado com sucesso')
        self._salvar()

    def _printar(self):
        for i, ven in enumerate(self):
            if i != 0 and self[i]['nome'] != self[i-1]['nome']:
                print('- ' * 15)
                print(f'{ven["codigo"]}: {ven["nome"]}  - mês: {ven["mes"]}, venda: {ven["venda"]}')
            else:
                print(f'{ven["codigo"]}: {ven["nome"]}  - mês: {ven["mes"]}, venda: {ven["venda"]}')

    def _apagar_arquivo(self):
        if os.path.exists(os.path.join(os.getcwd(), 'vendas.txt')):
            os.remove(os.path.join(os.getcwd(), 'vendas.txt'))


lista = Vendas()
