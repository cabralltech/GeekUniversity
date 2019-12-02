users = [
    {'username': 'samuel', 'tweets': ['I love cats', 'I love dogs']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': 'I love dogs'},
    {'username': 'guitar_gal', 'tweets': []}
]

names = sorted(users, key=lambda u: len(u['tweets']))
for i in names:
    print(i['username'])

l1 = ['name', 'age', 'city', 'email']
l2 = ['Mhirley', 40, 'Florianópolis', 'mhiloca@gmail.com']
d1 = list(zip(l1, l2))
print(d1)

cidades = [('Tóquio', 23), ('Londres', 14), ('Nova Iorque', 25), ('Calcutá', 36), ('Aucklan', 13)]
cid = dict(cidades)
print(cid)
print(list(zip(*cidades)))
print(list(zip(*d1)))
