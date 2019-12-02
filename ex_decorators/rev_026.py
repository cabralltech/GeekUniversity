from validacao import validar


@validar(ValueError)
def entrada():
    mat = int(input('Número de matrícula: ').strip())
    sobrenome = input('Sobrenome: ').strip().title()
    ano_nasc = int(input('Ano de nascimento: ').strip())
    return Alunx(mat=mat, sobrenome=sobrenome, ano_nasc=ano_nasc)


@validar(ValueError)
def cadastro():
    qtd = int(input('Quantos alunxs vc quer cadastrar? ').strip())
    cad = [entrada() for x in range(qtd)]
    with open('cadastro_alunxs.txt', 'w') as ca:
        for alunx in cad:
            ca.write(f'{alunx["mat"]:<5}: '
                     f'{alunx["sobrenome"]:<15}: '
                     f'{alunx["ano_nasc"]} \n')


class Alunx(dict):
    def __init__(self, mat, sobrenome, ano_nasc):
        super().__init__()
        self['mat'] = mat
        self['sobrenome'] = sobrenome
        self['ano_nasc'] = ano_nasc


cadastro()
# help(Alunx)