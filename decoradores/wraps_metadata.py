from functools import wraps


def ver_log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Eu sou uma função dentro da outra função"""
        print(f'Você está chamando a {fn.__name__}')
        print(f'Aqui está a documentação: {fn.__doc__}')
        return fn(*args, **kwargs)
    return wrapper


@ver_log
def somar(a, b):
    """Retorna a soma entre os args a e b"""
    return a + b


# print(somar(8, 4))
print(somar.__doc__)
print(somar.__name__)