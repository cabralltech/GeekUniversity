import datetime

# print(dir(datetime))

# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

# print(datetime.datetime.now())

nasc = input('Data de nascimento (dd/mm/aaaa): ').strip()
nasc = nasc.split('/')
data_nasc = datetime.date(
    year=int(nasc[2].strip()),
    month=int(nasc[1].strip()),
    day=int(nasc[0].strip())
)
print(data_nasc)
print(data_nasc.year)
print(dir(data_nasc))
