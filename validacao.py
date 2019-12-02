from functools import wraps


def validate(*types, err):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    nargs = []
                    for (a, t) in zip(args, types):
                        if type(a) == t:
                            nargs.append(a)
                        else:
                            nargs.append(t(a))
                    return func(*nargs, **kwargs)
                except err:
                    print('\033[31mDados inválidos\033[m Tente novamente')
        return wrapper
    return decorator


def validar(err):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except err:
                    print('\033[31mDados inválidos\033[m Tente novamente')
        return wrapper
    return decorator



def go_on(msg):
    while True:
        ans = input(f'Quer registrar outrx {msg}? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m Tente novamente')
        else:
            return ans

