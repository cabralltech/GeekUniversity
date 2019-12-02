def soma(a,b):
    assert a > 0 and b > 0, 'Ambos nºs precisam ser positvos'
    return a + b

#
# print(soma(4, 8))
# print(soma(-2, 7))


def comer_mal(msg):
    assert msg in (
        'pizza',
        'hamburguer',
        'sorvete',
        'batata-frita',
        'nuggets',
        'doces',
        'cachorro-quente'
    ), 'A comida precisa ser junkie-food'
    return f'Eu como {msg} todos os dias'


def poderes(user):
    assert user == 'admin', 'User precisa ser admin para ter poderes'
    # do something
    return 'Adeus'


comida = 'nuggets'
print(comer_mal(comida))

