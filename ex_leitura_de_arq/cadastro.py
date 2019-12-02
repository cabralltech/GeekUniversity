def validate(err):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return fn(*args, **kwargs)
                except err:
                    print('\033[31mERRO! Dados inválidos\033[m')
        return wrapper
    return decorator


def go_on(coisa):
    while True:
        ans = input(f'Quer registrar outrx {coisa}? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mResposta inválida\033[m')
        else:
            return ans

