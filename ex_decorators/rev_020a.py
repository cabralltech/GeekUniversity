from validacao import validar, go_on


@validar(ValueError)
def turma():
    num = int(input('Quantidade de aluxs: ').strip())
    nomes, notas = [], []
    for i in range(num):
        print('- ' * 5)
        nomes.append(input('Nome: ').strip().title())
        notas.append(float(input('Nota final: ').strip().replace(',', '.')))
    tur = zip(nomes, notas)
    return tur


lista = turma()
with open('turma.txt', 'w') as tu:
    for al in lista:
        tu.write(f'{al[0]:<40}{al[1]} \n')