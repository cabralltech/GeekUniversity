def validate(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


class Alunx(dict):
    @validate
    def __init__(self):
        super().__init__()
        self['nome'] = input('Nome: ').title().strip()
        self['nota'] = float(input('Nota final: ').replace(',', '.'))

    def __repr__(self):
        return f'{self["nome"]} - {self["nota"]} \n'


while True:
    try:
        qtd = int(input('Números de alunxs: '))
        break
    except ValueError:
        print('\033[31mERRO! Dados inválidos\033[m')
arte = [Alunx() for x in range(qtd)]
with open('binario.bin', 'w+b') as b:
    for i in arte:
        b.write(repr(i).encode())
with open('binario.bin', 'rb') as bn:
    rol = []
    for r in bn:
        ro = r.decode()
        ro = ro.split('-')
        ro = {'nome': ro[0], 'nota': float(ro[1].strip().replace('\n', ''))}
        rol.append(ro)
dados = sorted(rol, key=lambda a: a['nota'], reverse=True)
print(f'A maior nota é {dados[0]["nota"]} dx alunx {dados[0]["nome"]}')
