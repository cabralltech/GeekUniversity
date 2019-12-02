def polite(fn):
    def wrapper(nom):
        print('Olá,')
        print(fn(nom))
        print('Tenha um bom dia')
    return wrapper


def saudacao(p):
    return f'Meu nome é {p}'


def raiva(p):
    return f'Vai te fuder, {p}'


nome = 'Mhirley'
teste = polite(saudacao)
teste(nome)
teste2 = polite(raiva)
teste2(nome)


