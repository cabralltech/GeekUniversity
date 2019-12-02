paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ru': 'Reino Unido', 'ca': 'Canada'}
print(paises)

paises2 = dict(fra='França', es='Espanha', it='Italia')
print(paises2)

print(paises.get('br'))
print(paises.get('rus'))
"""
resp = None
while str(resp) not in 'NS':
    resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break
"""
pais = paises2.get('rus', 'inexistente')
print(f'Encontrei o país {pais}')

print('br' in paises)
print('rus' in paises)
print('Brasil' in paises)

nome = {}.fromkeys('a', 'Mhirley')
print(nome)

nome = {}.fromkeys(['nome', 'sobrenome'], 'indefinido')
print(nome)

exemplo = {}.fromkeys(['nome', 'sobrenome'], None)
print(exemplo)

exmp2 = {}.fromkeys(range(1, 10), None)
print(exmp2)

meses = ['jan', 'fev', 'mar']
renda = [250, 300, 450]
receita = {meses[i]: renda[i] for i in range(0, len(meses))}
print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])
    
