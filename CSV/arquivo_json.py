import jsonpickle

with open('misocial_1.txt') as file:
    bolsa = file.read()

familia = jsonpickle.decode(bolsa)
docs = familia.get('response')
doc = docs['docs']
it = iter(doc)
print(next(it))
res = filter(lambda a: a['anomes'] == '201301', doc)
resposta = sum(map(lambda b: b['qtd_familias_beneficiarias_bolsa_familia'], res))
print(resposta)
