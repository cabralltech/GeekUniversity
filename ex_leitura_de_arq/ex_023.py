def validate(fn):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


def go_on():
    while True:
        ans = input('Quer cadastrar outrx funcionarix? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            return ans


class Funcionarix:
    @validate
    def __init__(self):
        print('- ' * 15)
        self.nome = input('Nome: ').title().strip()
        self.prof = input('Profissão: ').strip().title()
        self.tempo = int(input('Tempo de serviço (em anos): '))

    def __repr__(self):
        return f'{self.nome:<40}{self.prof:<20}{self.tempo}'


with open('emp.txt', 'w') as em:
    while True:
        empr = Funcionarix()
        em.write(f'{repr(empr)} \n')
        if go_on() == 'N':
            break
