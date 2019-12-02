def validate(fun):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fun(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


def go_on():
    while True:
        ans = input('Quer cadastrar outro aluno? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            return ans


class Estudante:
    @validate
    def __init__(self):
        print('- ' * 15)
        self.nome = input('Nome: ').strip().upper()
        self.nota = float(input('Nota: ').replace(',', '.'))

    def __repr__(self):
        return f'NOME: {self.nome} NOTA: {self.nota}'


# with open('notas.txt', 'w') as n:
#     while True:
#         aluno = Estudante()
#         n.write(f'{repr(aluno)} \n')
#         if go_on() == 'N':
#             break
with open('notas.txt') as nt:
    lista =[]
    for dado in nt:
        alunx = dado.split()
        alunx = {'nome': alunx[1], 'nota': float(alunx[3])}
        lista.append(alunx)
print('- ' * 15)
print(f'A maior nota '
      f'é {max(lista, key=lambda a: a["nota"])["nota"]} '
      f'dx alunx {max(lista, key=lambda b: b["nota"])["nome"]}')
# values = [e.replace('\n', '') for e in alunxs.split() if e != 'NOME:' and e != 'NOTA:']
# keys = ['NOME', 'NOTA']
# final = int(len(values) / 2)
# rol = []
# for i in range(final):
#     rol.append({keys[a]: values[a] for a in range(2)})
#     values.pop(0)
#     values.pop(0)
# malu = max(rol, key=lambda x: float(x['NOTA']))['NOME']
# mant = max(rol, key=lambda y: float(y['NOTA']))['NOTA']
# print('- ' * 15)
# print(f'A maior nota é {mant} dx alunx {malu}')
