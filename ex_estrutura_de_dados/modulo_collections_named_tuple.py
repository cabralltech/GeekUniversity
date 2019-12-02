from collections import namedtuple
cachorro = namedtuple('cachorro', 'idade raça nome')
floffy = cachorro(idade=6, raça='terrier', nome= 'floffy')
print(floffy)
for i, v in enumerate(floffy):
    print(f'{i}: {v}')

print(floffy.nome)


