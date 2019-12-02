def validate(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


def go_on():
    while True:
        ans = input('Quer cadastrar outrx alunx? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            return ans


class Alunx(dict):
    @validate
    def __init__(self):
        super().__init__()
        self['nome'] = input('Nome: ').title().strip()
        self['nota'] = float(input('Nota final: ').replace(',', '.'))

    def __repr__(self):
        return f'{self["nome"]:<40}{self["nota"]}'


with open('notas_alunxs.txt', 'w') as n:
    n.write(f'{"NOME":<40}{"NOTA"} \n')
    while True:
        est = Alunx()
        n.write(f'{repr(est)} \n')
        if go_on() == 'N':
            break
