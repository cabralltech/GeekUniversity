def ensure_first_arg(value):
    def inner(func):
        def wrapper(*args, **kwargs):
            if args[0] == value :
                return func(*args, **kwargs)
            return 'Invalid value'
        return wrapper
    return inner


@ensure_first_arg(8)
def somar(a, b):
    return a + b


n1, n2 = 9, 9
print(somar(n1, n2))
