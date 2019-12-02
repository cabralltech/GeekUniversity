import datetime
"""
agora = datetime.datetime.now()
# print(repr(agora))
# print(dir(agora))
print(agora)
print('- ' * 15)
hoje = datetime.datetime.today()
# print(repr(hoje))
# print(dir(hoje))
print(hoje)
print(dir(datetime.datetime.now()))
manutencao = datetime.datetime.combine(datetime.datetime.now()+datetime.timedelta(days=1), datetime.time())
print(manutencao)
"""
nasc = input('Data nascimento (dd/mm/aaaa): ').strip()
# data_nasc = datetime.date(
#     year=int(nasc[2]),
#     month=int(nasc[1]),
#     day=int(nasc[0]),
# )
data_nasc = datetime.datetime.strptime(nasc, '%d/%m/%Y')
dias_semana = {
    0: 'segunda-feira',
    1: 'terça-feira',
    2: 'quarta-feira',
    3: 'quinta-feira',
    4: 'sexta-feira',
    5: 'sábado',
    6: 'domingo'
}
nasc_semana = dias_semana[data_nasc.weekday()]
nasc = data_nasc.strftime('%d/%m/%Y')
print(f'Você nasceu em {nasc} que foi um(a) {nasc_semana}')
