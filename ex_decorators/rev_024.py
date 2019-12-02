from validacao import validar, go_on
from os import path


class Produto(dict):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        print('- ' * 5)
        self['codigo'] = int(input('Código: ').strip())
        self['nome'] = input('Produto: ').strip().title()
        self['qtd'] = int(input('Quantidade: ').strip())

    def __repr__(self):
        return super().__repr__()


class Despensa(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        if path.exists('despensa.bin'):
            with open('despensa.bin', 'rb') as d:
                for p in d:
                    pr = p.decode().replace('\n', '').split(':')
                    produto = {
                        'codigo': int(pr[0].strip()),
                        'nome': pr[1].strip().title(),
                        'qtd': int(pr[2].strip())
                    }
                    self.append(produto)
        else:
            while True:
                self.append(Produto())
                if go_on('produto') == 'N':
                    break

    def __repr__(self):
        return super().__repr__()

    @validar(ValueError)
    def compra(self):
        compras = []
        while True:
            print('- ' * 15)
            cod = int(input('Insira código do produto: ').strip())
            for p in self:
                if cod == p['codigo']:
                    n = int(input(f'Quantidade de {p["nome"]} compradxs: ').strip())
                    p['qtd'] += n
                    compras.append({'nome': p['nome'], 'qtd': p['qtd']})
            if go_on('compra') == 'N':
                break
        print('- ' * 15)
        for c in compras:
            print(f'{c["nome"]}: {c["qtd"]}')

    @validar(ValueError)
    def usa(self):
        usados = []
        while True:
            print('- ' * 15)
            cod = int(input('Insira código do produto: ').strip())
            for p in self:
                if cod == p['codigo']:
                    n = int(input(f'Quantidade de {p["nome"]} usadxs: ').strip())
                    p['qtd'] -= n
                    usados.append({'nome': p['nome'], 'qtd': p['qtd']})
            if go_on('uso') == 'N':
                break
        print('- ' * 15)
        for u in usados:
            print(f'{u["nome"]}: {u["qtd"]}')

    def relatorio_final(self):
        with open('despensa.bin', 'w+b') as des:
            for pro in self:
                des.write(f'{pro["codigo"]}: '
                          f'{pro["nome"]:<30}: '
                          f'{pro["qtd"]} \n'.encode())

    def nao_tem(self):
        with open('indisponiveis.bin', 'w+b') as ind:
            for indis in self:
                if indis['qtd'] == 0:
                    ind.write(f'{indis["codigo"]}: '
                              f'{indis["nome"]} \n'.encode())


lista = Despensa()
lista.compra()
lista.usa()
lista.relatorio_final()
lista.nao_tem()

