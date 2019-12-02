from functools import wraps


def forcar_tipo(*tipos):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nargs = []
            for (arg, tipo) in zip(args, tipos):
                if type(arg) == tipo:
                    nargs.append(arg)
                else:
                    nargs.append(tipo(arg))
            return func(*nargs, **kwargs)
        return wrapper
    return decorador


@forcar_tipo(int, int)
def somar(a, b):
    return a + b


@forcar_tipo(str)
def gritar(msg):
    return msg.upper()


@forcar_tipo(str, int)
def repetir(nome, num):
    for i in range(num):
        print(nome * i)


print(somar('9', 8))
print(repetir('mhirley', '5'))