import cadastro as c


class Alunx:
    @c.validate(ValueError)
    def __init__(self):
        print('- ' * 15)
        self.mat = int(input('Número de matrícula: ').strip())
        self.sob = input('Sobrenome dx alunx: ').title().strip()
        self.nasc = int(input('Ano de nascimento [AAAA]: ').strip())

    def __repr__(self):
        return f'{self.mat:<10}{self.sob:<20}{self.nasc}'


class Registro(list):
    @c.validate(ValueError)
    def __init__(self):
        super().__init__()
        self.num = int(input('Quantos alunxs vc quer cadastrar? ').strip())
        for i in range(self.num):
            self.append(Alunx())

    def __repr__(self):
        return super().__repr__()


reg = Registro()
with open('alunxs_mat.txt', 'w') as am:
    for i in sorted(reg, key=lambda a: a.sob):
        am.write(f'{i} \n')
