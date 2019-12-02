from validacao import validar, go_on
import os


@validar(ValueError)
def entrada_vendedor():
    codigo_vendedor = int(input('Código do vendedor: ').strip())
    nome_vendedor = input('Nome do vendedor: ').strip().title()
    valor_venda = float(input('Valor da venda: ').strip().replace(',', '.'))
    mes = int(input('Mês: ').strip())
    return Vendedor(
        codigo=codigo_vendedor,
        nome=nome_vendedor,
        venda=valor_venda,
        mes=mes
    )


class Vendedor(dict):
    def __init__(self, codigo, nome, venda, mes):
        super().__init__()
        self['codigo'] = codigo
        self['nome'] = nome
        self['venda'] = venda
        self['mes'] = mes

    def __repr__(self):
        return super().__repr__()


class Arquivo(list):
    def __init__(self):
        super().__init__()
        self.pa = 'arquivo_vendas.txt'
        if os.path.exists(self.pa):
            with open(self.pa) as arquivo:
                for venda in arquivo:
                    venda = venda.replace('\n', '').split(':')
                    registro = Vendedor(
                        codigo=int(venda[0].strip()),
                        nome=venda[1].strip().title(),
                        venda=float(venda[2].strip()),
                        mes=int(venda[3].strip())

                    )
                    self.append(registro)
            self._menu()
            self._gravar()
        else:
            while True:
                self.append(entrada_vendedor())
                if go_on('registro') == 'N':
                    break
            self._gravar()

    def __repr__(self):
        return super().__repr__()

    @validar(ValueError)
    def _menu(self):
        menu = int(input('Escolha a operação:\n'
                         '[ 1 ] Criar arquivo\n'
                         '[ 2 ] Incluir registro\n'
                         '[ 3 ] Excluir vendedor\n'
                         '[ 4 ] Alterar valor de venda\n'
                         '[ 5 ] Imprimir registro na tela\n'
                         '[ 6 ] Excluir arquivo de dados\n'
                         '[ 7 ] Finalizar programa\n'
                         'Digite a opção: ').strip())
        print('- ' * 15)
        if menu == 1:
            self._gravar()
        elif menu == 2:
            vendedor_novo = entrada_vendedor()
            self.append(vendedor_novo)
            print(f'{vendedor_novo["nome"]} incluído com sucesso')
        elif menu == 3:
            self._excluir_vendedor()
        elif menu == 4:
            self._alterar_valor_venda()
        elif menu == 5:
            self._printar()
        elif menu == 6:
            os.remove(self.pa)
            return f'Arquivo {self.pa} removido com sucesso'
        elif menu == 7:
            print(f'{"FINALIZAR PROGRAMA":^30}')
            print('- ' * 15)

    def _gravar(self):
        with open(self.pa, 'w') as av:
            for registro in sorted(self, key=lambda a: a['nome']):
                av.write(f'{registro["codigo"]:<5}:'
                         f'{registro["nome"]:<40}:'
                         f'{registro["venda"]:<10}:'
                         f'{registro["mes"]} \n')

    @validar(ValueError)
    def _excluir_vendedor(self):
        nome_vendedor_del = input('Nome do vendedor a ser apagado: ').strip()
        for indice, registro in enumerate(self):
            if nome_vendedor_del in registro['nome'] or nome_vendedor_del == registro['nome']:
                print(f'- {registro["nome"]}')
                vendedor_apagado = self.pop(indice)
                print(f'{vendedor_apagado["nome"]} apagado com sucesso')

    @validar(ValueError)
    def _alterar_valor_venda(self):
        vendedor_venda = input('Nome do vendedor: ').strip().title()
        for registro in self:
            if vendedor_venda == registro['nome'] or vendedor_venda in registro['nome']:
                print(f'{registro["codigo"]:<5}:'
                      f'{registro["nome"]:<40}:'
                      f'{registro["venda"]}')
                novo_valor = float(input('Novo valor de venda:').strip().replace(',', '.'))
                registro['venda'] = novo_valor
                print('- ' * 5)
                print(f'Valor de venda alterado com sucesso:\n'
                      f'{registro["codigo"]:<5}: '
                      f'{registro["nome"]:<40}: '
                      f'{registro["venda"]:<10}Mês: '
                      f'{registro["mes"]}')

    def _printar(self):
        for registro in sorted(self, key=lambda a: a['nome']):
            print(f'{registro["codigo"]:<5}: '
                  f'{registro["nome"]:<40}: '
                  f'{registro["venda"]:<10}Mês: '
                  f'{registro["mes"]}')


if __name__ == '__main__':
    vendas = Arquivo()
