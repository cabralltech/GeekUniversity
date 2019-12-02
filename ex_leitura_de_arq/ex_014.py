from datetime import date


class Dados:
    def __init__(self):
        self.nome = input('Nome completo: ').strip().title()
        while True:
            try:
                dia, mes, ano = input('Data de nascimento: ').split('/')
                if len(dia) > 2 or len(mes) > 2 or len(ano) < 4:
                    print('\033[31mDados incorretos\033[m DD/MM/AAAA')
                else:
                    self.nasc = f'{dia}/{mes}/{ano}'
                    break
            except ValueError:
                print('\033[31mDados inválidos!\033[m Separe a data com "/"')


def go_on():
    ans = input('Quer cadastrar outra pessoa? ').strip().upper()[0]
    while not ans in 'NS':
        print('\033[31mResposta inválida\033[m')
    else:
        return ans


def age(dia, mes, ano):
    ano_atual = date.today().year
    mes_atual = date.today().month
    dia_atual = date.today().day
    if mes_atual <= mes:
        if dia_atual < dia:
            idade = ano_atual - (ano + 1)
        else:
            idade = ano_atual - ano
    else:
        idade = ano_atual - ano
    return idade


with open('data_de_nascimento.txt', 'a') as file:
    while True:
        dado = Dados()
        file.write(f'{dado.nome:<30}')
        file.write(f'{dado.nasc} \n')
        if go_on() == 'N':
            break
with open('data_de_nascimento.txt') as f:
    nom = f.readlines()
    f.seek(0)
    arq = f.read().split()
nomes = [y.split(' ' * 11)[0] for y in nom]
datas = (x for x in arq if x[0].isnumeric())
ida = (z.replace('/', ' ').split() for z in datas)
idades = [age(int(k[0]), int(k[1]), int(k[2])) for k in ida]
with open('idades.txt', 'a') as ida:
    for i in range(len(nomes)):
        ida.write(f'{nomes[i]:<30}{idades[i]} \n')


