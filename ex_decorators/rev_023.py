from validacao import validar


class Colaborador(dict):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        self['profissao'] = input('Profissão: ').strip().title()
        self['tempo'] = int(input('Tempo de serviço: ').strip())

    def __repr__(self):
        return f'{self["profissao"]:<30}{self["tempo"]} anos'


class Empresa(list):
    @validar(ValueError)
    def __init__(self):
        super().__init__()
        for e in range(5):
            print('- ' * 10)
            self.append(Colaborador())

    def __repr__(self):
        return super().__repr__()

    def gravar(self):
        with open('emp.txt', 'w') as emp:
            for em in self:
                emp.write(f'{em} \n')


lista = Empresa()
lista.gravar()