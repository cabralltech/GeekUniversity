def dobro(a):
    return a * 2


def data_extenso(data):
    mes = ('janeiro', 'fevereiro', 'março',
          'abril', 'maio', 'junho', 'julho',
           'agosto', 'setembro', 'outubro',
           'novembro', 'dezembro')
    data = data.split('/')
    mes_index = int(data[1]) - 1
    return f'{data[0]} de {mes[mes_index]} de {data[2]}'


nasc = input('Escreva a data de nascimento DD/MM/AAAA: ')
print(data_extenso(nasc))