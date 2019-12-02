from datetime import date


class Dados:
    def __init__(self):
        print('- ' * 15)
        self.nome = input('Nome completo: ').strip().title()
        while True:
            try:
                dia, mes, ano = input('Data de nascimento: ').split('/')
                if len(dia) > 2 or len(mes) > 2 or 4 > len(ano) < 4:
                    print('\033[31mDados incorretos\033[m Tente DD/MM/AAAA')
                else:
                    self.nasc = f'{dia}/{mes}/{ano}'
                    break
            except ValueError:
                print('\033[31mDados inválidos!\033[m Separe a data com "/"')


def go_on():
    while True:
        ans = input('Quer cadastrar outra pessoa? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            return ans


def age(dia, mes, ano):
    act_day = date.today().day
    act_month = date.today().month
    act_year = date.today().year
    if act_month <= mes:
        if act_day < dia:
            idade = act_year - (ano + 1)
        else:
            idade = act_year - ano
    else:
        idade = act_year - ano
    return idade


def arquivo_entrada():
    with open('arquivo_entrada.txt', 'a') as arq:
        while True:
            dado = Dados()
            arq.write(f'{dado.nome:<30}')
            arq.write(f'{dado.nasc} \n')
            if go_on() == 'N':
                return arq.name


def idade_sit(v):
    if v == 18:
        return 'Entrando na maior idade'
    elif v > 18:
        return 'Maior de idade'
    return 'Menor de idade'


def arquivo_saida(arq_ent, arq_sai):
    with open(arq_ent) as file:
        data = file.read().split()
        file.seek(0)
        nom = file.readlines()
    ds = (x for x in data if x[0].isnumeric())
    ns = [z.split(" " * 3)[0] for z in nom]
    datas = (k.replace('/', ' ').split() for k in ds)
    idades = [age(int(y[0]), int(y[1]), int(y[2])) for y in datas]
    with open(arq_sai, 'a') as saida:
        for p in range(len(ns)):
            saida.write(f'{ns[p]:<30}')
            saida.write(f'{idades[p]:<10}')
            saida.write(f'{idade_sit(idades[p])} \n')
    return saida.name


arq1 = arquivo_entrada()
var = input('Nome arquivo de saída: ').lower().strip()
var += '.txt'
arq2 = arquivo_saida(arq1, var)
