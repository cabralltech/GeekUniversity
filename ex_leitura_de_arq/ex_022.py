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
        print('- ' * 15)
        self['nome'] = input('Nome: ').strip().title()
        self['nota1'] = float(input('1ª Nota: ').replace(',', '.'))
        self['nota2'] = float(input('2ª Nota: ').replace(',', '.'))
        self['nota3'] = float(input('3ª Nota: ').replace(',', '.'))

    def __repr__(self):
        return f'{self["nome"]:<40}{self["nota1"]:<10}{self["nota2"]:<10}{self["nota3"]}'


# with open('notas_3.txt', 'w') as n3:
#     while True:
#         alu = Alunx()
#         n3.write(f'{alu} \n')
#         if go_on() == 'N':
#             break
with open('notas_3.txt') as nt3:
    nota = nt3.readlines()
nota.sort()
with open('notas_saida.txt', 'w') as nts:
    for i in nota:
        nts.write(f'{i}')
