from datetime import date

hoje = date.today()
aniver = input('Data de aniversário (dd/mm): ').strip()
aniver = aniver.split('/')
if int(aniver[1]) < date.today().month:
    year = date.today().year + 1
else:
    year = date.today().year
data_aniver = date(
    year=year,
    month=int(aniver[1].strip()),
    day=int(aniver[0].strip())
)
delta = data_aniver - hoje
print(delta.days)
